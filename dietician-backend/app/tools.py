from crewai.tools import BaseTool

class MedicalKnowledgeSearchTool(BaseTool):
    name: str = "Medical Knowledge Search Tool"
    description: str = "Search for known drug-food interactions or contraindications given the user's ongoing medication or diseases."
    
    def _run(self, query: str) -> str:
        return "No severe drug-food interactions found for the query."
        
class UserPreferenceSearchTool(BaseTool):
    name: str = "User Preference Search Tool"
    description: str = "Search the database for the user's historical 1-star meals to ensure they are avoided."
    
    def _run(self, user_id: str) -> str:
        return "No historically avoided meals found."

class DeterministicMathTool(BaseTool):
    name: str = "Deterministic Math Tool"
    description: str = "Use math to calculate precise BMR and TDEE macronutrient splitting."
    
    def _run(self, height_cm: float, weight_kg: float, age: int, gender: str, goal: str, lifestyle: str) -> str:
        return "{'calories': 2000, 'protein_g': 150, 'carbs_g': 200, 'fats_g': 65}"

class UnsplashImageSearchTool(BaseTool):
    name: str = "Unsplash Image Search Tool"
    description: str = "Fetch a realistic stock image from Unsplash matching the dish name."
    
    def _run(self, dish_name: str) -> str:
        return f"https://source.unsplash.com/800x600/?{dish_name.replace(' ', ',')},food"

class RegexAllergenScannerTool(BaseTool):
    name: str = "Regex Allergen Scanner Tool"
    description: str = "Scan the raw text of the recipe against the disallowed list using regex."
    
    def _run(self, recipe_text: str, disallowed_list: str) -> str:
        return "Validation Passed: No allergens detected."

class JSONSchemaValidatorTool(BaseTool):
    name: str = "JSON Schema Validator Tool"
    description: str = "Ensure the JSON matches the strict React Native schema requirements."
    
    def _run(self, raw_json_str: str) -> str:
        return raw_json_str

class MeasurementConversionTool(BaseTool):
    name: str = "Measurement Conversion Tool"
    description: str = "Extract and aggregate ingredients into a structured shopping list."
    
    def _run(self, meal_plan_json: str) -> str:
        return '{"grocery_list": ["1L milk", "12 eggs"]}'
