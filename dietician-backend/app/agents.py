import os
from crewai import Agent, LLM
from app.tools import (
    MedicalKnowledgeSearchTool,
    UserPreferenceSearchTool,
    DeterministicMathTool,
    UnsplashImageSearchTool,
    RegexAllergenScannerTool,
    JSONSchemaValidatorTool,
    MeasurementConversionTool
)

class DieticianAgents:
    def __init__(self):
        # Using CrewAI's native LLM class for cleaner integration with custom endpoints
        self.llm = LLM(
            model=os.getenv("LLM_MODEL", "hosted_vllm//home/llmapi/minimax-m2.5"), 
            temperature=0.2,
            base_url=os.getenv("OPENAI_BASE_URL", "http://10.9.4.151:8125/v1"),
            api_key=os.getenv("OPENAI_API_KEY", "dummy-key"),
            timeout=300
        )

    def medical_profile_analyzer(self):
        return Agent(
            role='Clinical Intake Specialist',
            goal='Identify contraindications, allergies, and medical restrictions from health data.',
            backstory='Your job is to ensure no diet harms the patient. You strictly parse their prior diseases and medications.',
            tools=[MedicalKnowledgeSearchTool()],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def memory_feedback_analyst(self):
        return Agent(
            role='Long-Term Preference Tracker',
            goal='Identify historically disliked meals to exclude from the new plan.',
            backstory='You maintain user happiness by ensuring they are never recommended a food they previously scored poorly.',
            tools=[UserPreferenceSearchTool()],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def nutritional_calculator(self):
        return Agent(
            role='Anthropometric Analyst',
            goal='Calculate precise macro-nutrients and BMR based on body metrics.',
            backstory='You are a rigid mathematician who calculates the exact grams of protein, carbs, and fats needed per day.',
            tools=[DeterministicMathTool()],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def dietary_strategist(self):
        return Agent(
            role='Parameter Compiler',
            goal="Reconcile the user's goals with medical and preference restrictions.",
            backstory='You act as the bridge, formatting the exact parameters required for generating the recipe.',
            tools=[],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def meal_plan_architect(self):
        return Agent(
            role='Generative Culinary AI',
            goal='Dynamically invent a 4-meal daily schedule combining Breakfast, Lunch, Snacks, and Dinner.',
            backstory='You invent customized delicious meals and use Unsplash to provide visual aesthetics for the app.',
            tools=[UnsplashImageSearchTool()],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def qa_clinical_reviewer(self):
        return Agent(
            role='Final Safety Auditor',
            goal='Guarantee zero allergen overlap and strict adherence to the medical profile.',
            backstory="You intercept the Meal Architect's output, double checking every single ingredient against the medical list.",
            tools=[RegexAllergenScannerTool()],
            allow_delegation=True,
            verbose=True,
            llm=self.llm
        )

    def formatting_publisher(self):
        return Agent(
            role='JSON Output Standardizer',
            goal='Format the approved meal plan into strict JSON format.',
            backstory='You strip all conversational text and output raw JSON payloads specifically typed for a mobile app.',
            tools=[JSONSchemaValidatorTool()],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def grocery_procurement_agent(self):
        return Agent(
            role='Supply Chain Calculator',
            goal='Extract every raw ingredient into a deduplicated shopping list.',
            backstory='You make life easy for the user by turning recipe ingredients into a practical grocery checklist.',
            tools=[MeasurementConversionTool()],
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )
