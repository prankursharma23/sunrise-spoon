from crewai import Task

class DieticianTasks:
    
    def analyze_medical_history(self, agent, payload):
        return Task(
            description=f'''Analyze the medical data: Diseases: {payload.get("prior_diseases")}, Allergies: {payload.get("food_allergies")}, Medications: {payload.get("ongoing_medication")}
            Extract all food restrictions and produce a strict "Disallowed Ingredients" list.''',
            expected_output="A structured list of ingredients the user must NEVER consume.",
            agent=agent
        )

    def analyze_user_history(self, agent, payload):
        return Task(
            description=f'''Search for the user history: {payload.get("user_id")} to find previously disliked meals.''',
            expected_output="A string of recipes/ingredients to avoid because the user hates them.",
            agent=agent
        )

    def calculate_macros(self, agent, payload):
        return Task(
            description=f'''Use math to calculate macros for a {payload.get("gender")}, height {payload.get("height")}cm, weight {payload.get("weight")}kg, goal {payload.get("diet_goal")}, lifestyle {payload.get("lifestyle")}.''',
            expected_output="A JSON format string reflecting daily caloric target and macronutrient grams.",
            agent=agent
        )

    def compile_dietary_parameters(self, agent, payload):
        return Task(
            description=f'''Merge the outputs of the medical task, memory task, and math task, integrating the user's preference: {payload.get("food_preference")}.''',
            expected_output="The final architectural outline for the chef: Macros, Allowed Foods, Avoided Foods.",
            agent=agent
        )

    def invent_meal_plan(self, agent):
        return Task(
            description='''Take the parameters compiled by the stategist and invent a 4-meal plan consisting of Breakfast, Lunch, Snacks, Dinner. Fetch an image URL for each using the Unsplash tool.''',
            expected_output="A highly detailed list of 4 recipes, complete with ingredients, instructions, and an image URL each.",
            agent=agent
        )

    def audit_meal_plan(self, agent):
        return Task(
            description='''Take the 4 generated meals and strictly verify they do not contain any disallowed ingredients identified in the medical history.''',
            expected_output="The exact same meal plan, passing a final safety seal of approval.",
            agent=agent
        )

    def format_json_output(self, agent):
        return Task(
            description='''Translate the approved meal plan into a clean JSON array of objects representing meals. No markdown.''',
            expected_output="A pure JSON array.",
            agent=agent
        )

    def generate_grocery_list(self, agent):
        return Task(
            description='''Using the final approved meal plan, aggregate the raw ingredients into a Grocery List JSON block.''',
            expected_output="A pure JSON block containing an array grocery_list.",
            agent=agent
        )
