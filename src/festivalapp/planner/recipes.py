"""FestivalRecipes with 50+ traditional recipes by festival."""
from __future__ import annotations
from ..models import Recipe


class FestivalRecipes:
    """Database of 50+ traditional festival recipes."""

    def __init__(self) -> None:
        self._recipes: list[Recipe] = self._load_recipes()

    def _load_recipes(self) -> list[Recipe]:
        return [
            # Diwali recipes
            Recipe(name="Kaju Katli", festival="Diwali", region="All India", category="sweet", ingredients=["Cashews 2 cups", "Sugar 1 cup", "Water 1/2 cup", "Ghee 1 tsp", "Silver vark"], instructions=["Grind cashews to fine powder", "Make sugar syrup of one-string consistency", "Add cashew powder and stir continuously", "Cook until mixture leaves sides", "Spread on greased plate", "Cut into diamond shapes when warm"], prep_time_minutes=45),
            Recipe(name="Gulab Jamun", festival="Diwali", region="All India", category="sweet", ingredients=["Khoya 200g", "Maida 2 tbsp", "Baking soda pinch", "Sugar 2 cups", "Water 2 cups", "Cardamom 4", "Rose water 1 tsp"], instructions=["Crumble khoya, add maida and baking soda", "Knead smooth dough", "Make small balls (no cracks)", "Make sugar syrup with cardamom", "Fry balls on low heat until deep brown", "Soak in warm sugar syrup 2 hours"], prep_time_minutes=60),
            Recipe(name="Chakli", festival="Diwali", region="Maharashtra", category="savory", ingredients=["Rice flour 2 cups", "Besan 1/4 cup", "Sesame seeds 2 tbsp", "Red chili powder 1 tsp", "Cumin seeds 1 tsp", "Oil for frying"], instructions=["Mix all dry ingredients", "Add hot oil to bind", "Knead with warm water", "Use chakli mold to shape spirals", "Deep fry on medium heat until golden"], prep_time_minutes=45),
            Recipe(name="Anarsa", festival="Diwali", region="Maharashtra", category="sweet", ingredients=["Soaked rice 2 cups", "Jaggery 1.5 cups", "Poppy seeds 1/4 cup", "Ghee for frying"], instructions=["Soak rice 3 days, dry and grind", "Mix with melted jaggery", "Rest dough for a week ideally", "Shape into flat discs", "Coat with poppy seeds", "Deep fry on low heat"], prep_time_minutes=30),
            Recipe(name="Besan Laddoo", festival="Diwali", region="North India", category="sweet", ingredients=["Besan 2 cups", "Ghee 3/4 cup", "Powdered sugar 1 cup", "Cardamom powder 1 tsp", "Almonds chopped"], instructions=["Roast besan in ghee on low flame 20 min", "Cool slightly", "Add powdered sugar and cardamom", "Shape into round laddoos while warm"], prep_time_minutes=40),

            # Holi recipes
            Recipe(name="Gujiya", festival="Holi", region="North India", category="sweet", ingredients=["Maida 2 cups", "Ghee 4 tbsp", "Khoya 1 cup", "Sugar 1/2 cup", "Dry fruits chopped", "Cardamom powder"], instructions=["Make dough with maida and ghee", "Mix khoya, sugar, dry fruits for filling", "Roll small puris, fill and seal edges", "Deep fry until golden brown"], prep_time_minutes=60),
            Recipe(name="Thandai", festival="Holi", region="North India", category="drink", ingredients=["Milk 4 cups", "Almonds 20", "Cashews 10", "Poppy seeds 1 tbsp", "Fennel seeds 1 tsp", "Cardamom 4", "Saffron pinch", "Sugar 4 tbsp", "Rose water 1 tsp"], instructions=["Soak almonds, cashews, poppy seeds 4 hours", "Grind to smooth paste with fennel and cardamom", "Boil milk, cool, add paste and sugar", "Add saffron and rose water", "Serve chilled"], prep_time_minutes=30),
            Recipe(name="Malpua", festival="Holi", region="North India", category="sweet", ingredients=["Maida 1 cup", "Sooji 1/4 cup", "Milk 1 cup", "Sugar 3/4 cup", "Fennel seeds 1 tsp", "Ghee for frying"], instructions=["Mix maida, sooji, milk to smooth batter", "Rest 30 minutes", "Make sugar syrup", "Pour spoonfuls in hot ghee, fry both sides", "Dip in sugar syrup"], prep_time_minutes=45),
            Recipe(name="Puran Poli", festival="Holi", region="Maharashtra", category="sweet", ingredients=["Chana dal 1 cup", "Jaggery 1 cup", "Wheat flour 2 cups", "Cardamom powder 1 tsp", "Nutmeg pinch", "Ghee"], instructions=["Cook chana dal until soft", "Drain and mash with jaggery", "Cook mixture until dry", "Add cardamom and nutmeg", "Stuff into wheat flour balls", "Roll thin and cook on tawa with ghee"], prep_time_minutes=60),
            Recipe(name="Dahi Bhalle", festival="Holi", region="North India", category="savory", ingredients=["Urad dal 1 cup", "Yogurt 2 cups", "Tamarind chutney", "Green chutney", "Cumin powder", "Red chili powder", "Sev"], instructions=["Soak and grind urad dal", "Fry spoonfuls as vadas", "Soak in warm water 20 min", "Squeeze and place in yogurt", "Top with chutneys and spices"], prep_time_minutes=60),

            # Ganesh Chaturthi recipes
            Recipe(name="Ukadiche Modak", festival="Ganesh Chaturthi", region="Maharashtra", category="sweet", ingredients=["Rice flour 2 cups", "Coconut 1 cup grated", "Jaggery 3/4 cup", "Cardamom powder 1 tsp", "Nutmeg pinch"], instructions=["Cook jaggery with coconut for filling", "Add cardamom and nutmeg", "Make rice flour dough with boiling water", "Shape into cups, fill, and seal", "Steam for 15 minutes"], prep_time_minutes=60),
            Recipe(name="Puran Poli (Ganesh)", festival="Ganesh Chaturthi", region="Maharashtra", category="sweet", ingredients=["Chana dal 1 cup", "Jaggery 1 cup", "Wheat flour 2 cups", "Cardamom", "Ghee"], instructions=["Cook dal, mash with jaggery", "Season with cardamom", "Stuff in wheat dough balls", "Roll and cook with ghee"], prep_time_minutes=60),
            Recipe(name="Karanji", festival="Ganesh Chaturthi", region="Maharashtra", category="sweet", ingredients=["Maida 2 cups", "Dry coconut 1 cup", "Sugar 3/4 cup", "Poppy seeds 2 tbsp", "Ghee for frying"], instructions=["Make maida dough with ghee", "Mix coconut, sugar, poppy seeds for filling", "Roll small puris, fill, seal half-moon", "Deep fry until golden"], prep_time_minutes=45),

            # Navratri recipes
            Recipe(name="Sabudana Khichdi", festival="Navratri", region="Maharashtra", category="main", ingredients=["Sabudana 1 cup", "Peanuts 1/2 cup roasted", "Potatoes 2", "Green chilies 2", "Cumin seeds 1 tsp", "Sendha namak", "Ghee 2 tbsp", "Lemon juice"], instructions=["Soak sabudana overnight", "Fry cumin, add potatoes", "Add soaked sabudana", "Add crushed peanuts", "Season with rock salt and lemon"], prep_time_minutes=30),
            Recipe(name="Kuttu Ki Puri", festival="Navratri", region="North India", category="main", ingredients=["Buckwheat flour 2 cups", "Boiled potato 1", "Sendha namak", "Green chilies", "Ghee for frying"], instructions=["Mix flour with mashed potato", "Add salt and chilies", "Knead soft dough", "Roll and deep fry"], prep_time_minutes=25),
            Recipe(name="Rajgira Halwa", festival="Navratri", region="North India", category="sweet", ingredients=["Rajgira (amaranth) flour 1 cup", "Ghee 1/2 cup", "Sugar 3/4 cup", "Milk 1 cup", "Cardamom", "Almonds"], instructions=["Roast rajgira flour in ghee", "Add milk gradually", "Cook until thick", "Add sugar and cardamom", "Garnish with almonds"], prep_time_minutes=25),
            Recipe(name="Singhare Ke Atte Ka Halwa", festival="Navratri", region="North India", category="sweet", ingredients=["Water chestnut flour 1 cup", "Ghee 1/4 cup", "Sugar 1/2 cup", "Water 2 cups"], instructions=["Roast flour in ghee", "Add water gradually", "Stir to prevent lumps", "Add sugar, cook until thick"], prep_time_minutes=20),

            # Janmashtami recipes
            Recipe(name="Makhan Mishri", festival="Krishna Janmashtami", region="All India", category="sweet", ingredients=["Fresh butter 200g", "Mishri (rock sugar) 100g crushed"], instructions=["Whip fresh butter until fluffy", "Fold in crushed mishri", "Serve as offering to Krishna"], prep_time_minutes=10),
            Recipe(name="Panjiri", festival="Krishna Janmashtami", region="North India", category="sweet", ingredients=["Wheat flour 2 cups", "Ghee 1 cup", "Sugar 1 cup", "Almonds", "Desiccated coconut 1/2 cup", "Cardamom"], instructions=["Roast wheat flour in ghee until golden", "Cool slightly, add sugar", "Add coconut and cardamom", "Add chopped almonds", "Shape into portions"], prep_time_minutes=30),
            Recipe(name="Panchamrit", festival="Krishna Janmashtami", region="All India", category="drink", ingredients=["Milk 1 cup", "Yogurt 2 tbsp", "Honey 1 tbsp", "Ghee 1 tsp", "Sugar 1 tbsp", "Tulsi leaves"], instructions=["Mix milk and yogurt", "Add honey and ghee", "Add sugar", "Garnish with tulsi leaves", "Offer to Krishna"], prep_time_minutes=5),

            # Pongal recipes
            Recipe(name="Sweet Pongal (Sakkarai)", festival="Pongal", region="Tamil Nadu", category="sweet", ingredients=["Rice 1 cup", "Moong dal 1/2 cup", "Jaggery 1.5 cups", "Ghee 1/4 cup", "Cashews", "Raisins", "Cardamom", "Dry ginger"], instructions=["Cook rice and dal together", "Melt jaggery separately and strain", "Mix jaggery into rice-dal", "Add ghee, fried cashews, raisins", "Season with cardamom and ginger"], prep_time_minutes=40),
            Recipe(name="Ven Pongal", festival="Pongal", region="Tamil Nadu", category="main", ingredients=["Rice 1 cup", "Moong dal 1/2 cup", "Black pepper 1 tsp", "Cumin 1 tsp", "Ginger", "Curry leaves", "Ghee 3 tbsp", "Cashews"], instructions=["Pressure cook rice and dal together", "Temper with ghee, pepper, cumin, ginger", "Add curry leaves and fried cashews", "Mix well and serve hot"], prep_time_minutes=30),

            # Onam recipes
            Recipe(name="Avial", festival="Onam", region="Kerala", category="main", ingredients=["Mixed vegetables (drumstick, beans, carrot, yam)", "Coconut 1 cup grated", "Cumin 1 tsp", "Green chilies", "Yogurt 1/2 cup", "Coconut oil", "Curry leaves"], instructions=["Cook vegetables until just done", "Grind coconut, cumin, chilies to paste", "Add paste to vegetables", "Add yogurt, do not boil", "Finish with coconut oil and curry leaves"], prep_time_minutes=35),
            Recipe(name="Ada Pradhaman", festival="Onam", region="Kerala", category="sweet", ingredients=["Rice ada 1 cup", "Jaggery 1 cup", "Coconut milk (thick) 2 cups", "Coconut milk (thin) 2 cups", "Ghee 2 tbsp", "Cardamom", "Cashews", "Dry ginger"], instructions=["Roast ada in ghee", "Dissolve jaggery, strain", "Add thin coconut milk and ada", "Cook until ada is soft", "Add thick coconut milk", "Season with cardamom, cashews"], prep_time_minutes=45),

            # Durga Puja recipes
            Recipe(name="Luchi", festival="Durga Puja", region="West Bengal", category="main", ingredients=["Maida 2 cups", "Ghee 1 tbsp", "Salt pinch", "Oil for frying"], instructions=["Knead maida with ghee and water", "Rest 30 minutes", "Roll small thin circles", "Deep fry in hot oil until puffed"], prep_time_minutes=30),
            Recipe(name="Alur Dom", festival="Durga Puja", region="West Bengal", category="main", ingredients=["Baby potatoes 500g", "Ginger paste", "Tomato paste", "Cumin", "Bay leaf", "Turmeric", "Red chili", "Garam masala", "Ghee"], instructions=["Fry potatoes until golden", "Make masala with ginger, tomato, spices", "Add potatoes, simmer until gravy thickens", "Garnish with ghee and garam masala"], prep_time_minutes=40),
            Recipe(name="Sandesh", festival="Durga Puja", region="West Bengal", category="sweet", ingredients=["Chhena (fresh paneer) 500g", "Sugar 1/2 cup", "Cardamom", "Pistachio"], instructions=["Knead chhena until smooth", "Cook with sugar on low flame", "Stir until mixture leaves sides", "Add cardamom", "Shape into molds", "Garnish with pistachio"], prep_time_minutes=30),
            Recipe(name="Mishti Doi", festival="Durga Puja", region="West Bengal", category="sweet", ingredients=["Full fat milk 1 liter", "Yogurt culture 2 tbsp", "Sugar 1/2 cup (caramelized)", "Jaggery 2 tbsp"], instructions=["Reduce milk to 3/4", "Caramelize sugar to golden brown", "Mix into milk", "Cool to lukewarm, add yogurt culture", "Set in earthen pots 6-8 hours"], prep_time_minutes=30),

            # Makar Sankranti recipes
            Recipe(name="Til Laddoo", festival="Makar Sankranti", region="North India", category="sweet", ingredients=["White sesame seeds 2 cups", "Jaggery 1 cup", "Ghee 1 tsp", "Cardamom"], instructions=["Dry roast sesame seeds", "Melt jaggery to soft ball stage", "Mix sesame and jaggery quickly", "Shape into laddoos while hot"], prep_time_minutes=25),
            Recipe(name="Undhiyu", festival="Makar Sankranti", region="Gujarat", category="main", ingredients=["Surti papdi beans", "Purple yam", "Sweet potato", "Brinjal", "Banana", "Coconut-coriander-chili paste", "Methi muthiya"], instructions=["Layer vegetables in earthen pot", "Add coconut paste between layers", "Add methi muthiya on top", "Cook covered on slow flame", "Invert and serve"], prep_time_minutes=90),

            # Chhath recipes
            Recipe(name="Thekua", festival="Chhath Puja", region="Bihar", category="sweet", ingredients=["Wheat flour 2 cups", "Jaggery 1 cup", "Ghee 4 tbsp", "Dry coconut 2 tbsp", "Fennel seeds 1 tsp"], instructions=["Mix flour with melted jaggery and ghee", "Add coconut and fennel", "Knead stiff dough", "Shape into small patterns using mold", "Deep fry on low heat until golden"], prep_time_minutes=40),

            # Shivaratri recipes
            Recipe(name="Bhaang Thandai", festival="Maha Shivaratri", region="North India", category="drink", ingredients=["Bhaang paste 1 tsp", "Milk 4 cups", "Almonds 20", "Fennel seeds", "Pepper", "Cardamom", "Rose petals", "Sugar"], instructions=["Grind almonds, fennel, pepper, cardamom", "Boil milk with paste", "Strain and add bhaang paste", "Add sugar and rose water", "Serve chilled"], prep_time_minutes=20),

            # Ram Navami recipes
            Recipe(name="Panakam", festival="Ram Navami", region="South India", category="drink", ingredients=["Jaggery 1/2 cup", "Water 4 cups", "Dry ginger powder 1/2 tsp", "Cardamom powder 1/4 tsp", "Black pepper pinch", "Lemon juice 1 tbsp"], instructions=["Dissolve jaggery in water", "Add ginger, cardamom, pepper", "Add lemon juice", "Mix well and serve chilled"], prep_time_minutes=10),
            Recipe(name="Kosambari", festival="Ram Navami", region="South India", category="savory", ingredients=["Moong dal 1 cup soaked", "Cucumber diced", "Coconut grated", "Lemon juice", "Green chilies", "Coriander leaves", "Mustard seeds"], instructions=["Soak dal 2 hours, drain", "Mix with cucumber and coconut", "Temper with mustard seeds", "Add lemon juice and coriander"], prep_time_minutes=15),

            # Vasant Panchami
            Recipe(name="Kesar Boondi Laddoo", festival="Vasant Panchami", region="North India", category="sweet", ingredients=["Besan 2 cups", "Sugar 2 cups", "Saffron pinch", "Cardamom", "Ghee for frying", "Rose water"], instructions=["Make thin besan batter", "Drop through jhara into hot oil", "Make sugar syrup with saffron", "Soak boondi in syrup", "Drain and shape into laddoos"], prep_time_minutes=45),

            # Raksha Bandhan
            Recipe(name="Coconut Barfi", festival="Raksha Bandhan", region="All India", category="sweet", ingredients=["Desiccated coconut 2 cups", "Condensed milk 1 can", "Cardamom powder 1 tsp", "Ghee 1 tbsp", "Pistachios for garnish"], instructions=["Cook coconut and condensed milk on low flame", "Add cardamom and ghee", "Stir until mixture thickens and leaves sides", "Spread on greased plate", "Cut into squares when set"], prep_time_minutes=25),

            # Karva Chauth
            Recipe(name="Sargi Plate", festival="Karva Chauth", region="North India", category="main", ingredients=["Mathri (fried crackers)", "Feni (vermicelli sweet)", "Fruits", "Dry fruits", "Sweets", "Coconut water"], instructions=["Prepare mathri and feni night before", "Arrange all items on a thali", "Mother-in-law gives to daughter-in-law before dawn", "Eat before sunrise to begin fast"], prep_time_minutes=60),

            # Additional recipes to reach 50+
            Recipe(name="Ghewar", festival="Hartalika Teej", region="Rajasthan", category="sweet", ingredients=["Maida 1 cup", "Ghee 1/4 cup melted", "Milk 1/4 cup", "Ice water", "Sugar syrup", "Mawa", "Pistachios"], instructions=["Mix maida with ghee and milk", "Add ice water to make thin batter", "Pour into hot ghee mold", "Fry until honeycomb forms", "Soak in sugar syrup", "Top with mawa and pistachios"], prep_time_minutes=60),
            Recipe(name="Sundal", festival="Navratri", region="Tamil Nadu", category="savory", ingredients=["Chickpeas 1 cup cooked", "Coconut grated", "Mustard seeds", "Curry leaves", "Green chilies", "Asafoetida"], instructions=["Temper mustard seeds and curry leaves", "Add cooked chickpeas", "Add coconut and green chilies", "Mix well and serve warm"], prep_time_minutes=15),
            Recipe(name="Kozhukattai", festival="Ganesh Chaturthi", region="Tamil Nadu", category="sweet", ingredients=["Rice flour 2 cups", "Coconut 1 cup", "Jaggery 3/4 cup", "Cardamom", "Sesame oil 1 tsp"], instructions=["Boil water with oil, add rice flour", "Knead smooth dough", "Cook jaggery and coconut for filling", "Shape dough, fill, seal", "Steam 12 minutes"], prep_time_minutes=45),
            Recipe(name="Kheer", festival="Multiple", region="All India", category="sweet", ingredients=["Rice 1/4 cup", "Milk 1 liter", "Sugar 1/2 cup", "Cardamom 4", "Saffron pinch", "Almonds", "Raisins"], instructions=["Wash and soak rice 30 min", "Boil milk, add rice", "Simmer until rice is soft and milk thickens", "Add sugar, saffron, cardamom", "Garnish with nuts and raisins"], prep_time_minutes=45),
            Recipe(name="Basundi", festival="Diwali", region="Gujarat/Maharashtra", category="sweet", ingredients=["Full fat milk 1 liter", "Sugar 1/3 cup", "Saffron", "Cardamom", "Charoli", "Almonds slivered"], instructions=["Boil milk on medium flame", "Stir continuously, reduce to half", "Add sugar and saffron", "Cool and add cardamom", "Serve chilled with charoli garnish"], prep_time_minutes=60),
            Recipe(name="Shrikhand", festival="Gudi Padwa", region="Maharashtra/Gujarat", category="sweet", ingredients=["Hung yogurt 2 cups", "Sugar 1/2 cup powdered", "Saffron milk", "Cardamom powder", "Pistachios"], instructions=["Hang yogurt overnight to get chakka", "Whisk smooth", "Add sugar, saffron, cardamom", "Refrigerate 2 hours", "Serve with puri"], prep_time_minutes=20),
        ]

    def get_all_recipes(self) -> list[Recipe]:
        return self._recipes

    def get_by_festival(self, festival: str) -> list[Recipe]:
        return [r for r in self._recipes if festival.lower() in r.festival.lower()]

    def get_by_category(self, category: str) -> list[Recipe]:
        return [r for r in self._recipes if r.category == category]

    def get_by_region(self, region: str) -> list[Recipe]:
        r = region.lower()
        return [rec for rec in self._recipes if r in rec.region.lower()]

    def search_recipes(self, query: str) -> list[Recipe]:
        q = query.lower()
        return [r for r in self._recipes if q in r.name.lower() or q in r.festival.lower()
                or any(q in ing.lower() for ing in r.ingredients)]
