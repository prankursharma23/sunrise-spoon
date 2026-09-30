import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from crewai import Crew, Process
from app.agents import DieticianAgents
from app.tasks import DieticianTasks

load_dotenv()

app = FastAPI(title="Sunrise Spoon Backend", description="CrewAI Dietician API")

class AssessmentPayload(BaseModel):
    user_id: str
    height: float
    weight: float
    target_weight: float
    gender: str
    diet_goal: str
    food_preference: str
    lifestyle: str
    prior_diseases: str
    food_allergies: str
    ongoing_medication: str

@app.post("/generate-plan")
async def generate_diet_plan(payload: AssessmentPayload):
    try:
        agents = DieticianAgents()
        tasks = DieticianTasks()

        # Initialize Agents
        medical_agent = agents.medical_profile_analyzer()
        memory_agent = agents.memory_feedback_analyst()
        math_agent = agents.nutritional_calculator()
        strategist_agent = agents.dietary_strategist()
        architect_agent = agents.meal_plan_architect()
        qa_agent = agents.qa_clinical_reviewer()
        formatter_agent = agents.formatting_publisher()
        grocery_agent = agents.grocery_procurement_agent()

        # Initialize Tasks
        # (Pass the specific payload data into the tasks)
        medical_task = tasks.analyze_medical_history(medical_agent, payload.dict())
        memory_task = tasks.analyze_user_history(memory_agent, payload.dict())
        math_task = tasks.calculate_macros(math_agent, payload.dict())
        strategy_task = tasks.compile_dietary_parameters(strategist_agent, payload.dict())
        architect_task = tasks.invent_meal_plan(architect_agent)
        qa_task = tasks.audit_meal_plan(qa_agent)
        formatter_task = tasks.format_json_output(formatter_agent)
        grocery_task = tasks.generate_grocery_list(grocery_agent)

        # Build Crew
        crew = Crew(
            agents=[
                medical_agent, memory_agent, math_agent, strategist_agent, 
                architect_agent, qa_agent, formatter_agent, grocery_agent
            ],
            tasks=[
                medical_task, memory_task, math_task, strategy_task, 
                architect_task, qa_task, formatter_task, grocery_task
            ],
            process=Process.sequential,
            verbose=True
        )

        result = crew.kickoff()
        
        return {
            "status": "success",
            "message": "Crew finished generating the custom diet plan.",
            "data": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
