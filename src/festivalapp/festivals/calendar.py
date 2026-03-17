"""FestivalCalendar with 30+ Hindu festivals and dates."""
from __future__ import annotations
from ..models import FestivalDetail


class FestivalCalendar:
    """Calendar of 30+ Hindu festivals with timing information."""

    def __init__(self) -> None:
        self._festivals: list[FestivalDetail] = self._load_festivals()

    def _load_festivals(self) -> list[FestivalDetail]:
        return [
            FestivalDetail(name="Makar Sankranti", month="January", duration_days=1, significance="Sun enters Capricorn; harvest festival marking Uttarayana", deity="Surya", tithi="14 January (solar)", regions=["All India"], rituals=["Surya Puja", "Til-gul distribution", "Kite flying"], foods=["Til laddoo", "Gur chikki", "Khichdi", "Pongal"], greetings=["Happy Sankranti", "Til gul ghya god god bola"]),
            FestivalDetail(name="Lohri", month="January", duration_days=1, significance="Bonfire festival celebrating winter harvest in Punjab", deity="Agni", tithi="13 January", regions=["Punjab", "Haryana", "Delhi"], rituals=["Bonfire", "Dancing bhangra", "Circling the fire"], foods=["Rewri", "Gajak", "Popcorn", "Peanuts", "Sarson da saag", "Makki di roti"]),
            FestivalDetail(name="Pongal", month="January", duration_days=4, significance="Tamil harvest festival thanking Sun God and cattle", deity="Surya", tithi="14-17 January", regions=["Tamil Nadu", "Andhra Pradesh", "Karnataka"], rituals=["Boiling rice until it overflows", "Cattle decoration", "Kolam drawing"], foods=["Sweet Pongal", "Ven Pongal", "Sakkarai Pongal", "Vadai"]),
            FestivalDetail(name="Vasant Panchami", month="January/February", duration_days=1, significance="Celebration of spring and Goddess Saraswati", deity="Saraswati", tithi="Magha Shukla Panchami", regions=["All India"], rituals=["Saraswati Puja", "Wearing yellow", "Placing books near idol"], foods=["Yellow rice", "Yellow sweets", "Boondi laddoo"]),
            FestivalDetail(name="Maha Shivaratri", month="February/March", duration_days=1, significance="The great night of Lord Shiva - night of spiritual awakening", deity="Shiva", tithi="Phalguna Krishna Chaturdashi", regions=["All India"], rituals=["Night-long vigil", "Shivalinga Abhishek", "Fasting", "Rudra chanting"], foods=["Fruits only (fasting)", "Thandai", "Bhaang"]),
            FestivalDetail(name="Holi", month="March", duration_days=2, significance="Festival of colors celebrating spring, love, and victory of good over evil", deity="Krishna", tithi="Phalguna Purnima", regions=["All India"], rituals=["Holika Dahan bonfire", "Playing with colors", "Singing Holi songs"], foods=["Gujiya", "Thandai", "Malpua", "Puran Poli", "Dahi Bhalle"], greetings=["Happy Holi", "Holi hai!"]),
            FestivalDetail(name="Ugadi", month="March/April", duration_days=1, significance="Telugu and Kannada New Year", deity="Brahma", tithi="Chaitra Shukla Pratipada", regions=["Andhra Pradesh", "Telangana", "Karnataka"], rituals=["Panchanga Shravan", "Neem-jaggery eating", "Rangoli"], foods=["Ugadi Pachadi (6 tastes)", "Pulihora", "Bobbatlu", "Holige"]),
            FestivalDetail(name="Gudi Padwa", month="March/April", duration_days=1, significance="Marathi New Year", deity="Brahma", tithi="Chaitra Shukla Pratipada", regions=["Maharashtra", "Goa", "Konkan"], rituals=["Raising Gudi flag", "Rangoli", "New clothes"], foods=["Shrikhand Puri", "Puran Poli", "Aamras"]),
            FestivalDetail(name="Ram Navami", month="March/April", duration_days=1, significance="Birthday of Lord Rama, seventh avatar of Vishnu", deity="Rama", tithi="Chaitra Shukla Navami", regions=["All India"], rituals=["Rama Puja at noon", "Ramayana reading", "Fasting"], foods=["Panakam (jaggery drink)", "Kosambari", "Fruits", "Sundal"]),
            FestivalDetail(name="Hanuman Jayanti", month="April", duration_days=1, significance="Birthday of Lord Hanuman, divine devotee of Rama", deity="Hanuman", tithi="Chaitra Purnima", regions=["All India"], rituals=["Hanuman Chalisa recitation", "Sindoor offering", "Visiting Hanuman temples"], foods=["Boondi laddoo", "Bananas", "Prasad"]),
            FestivalDetail(name="Akshaya Tritiya", month="April/May", duration_days=1, significance="Day of unending prosperity; extremely auspicious for new beginnings", deity="Vishnu", tithi="Vaishakha Shukla Tritiya", regions=["All India"], rituals=["Gold purchase", "Starting new ventures", "Charity"], foods=["Special puja prasad", "Kheer"]),
            FestivalDetail(name="Rath Yatra", month="June/July", duration_days=9, significance="Chariot procession of Lord Jagannath from Puri", deity="Jagannath (Krishna)", tithi="Ashadha Shukla Dwitiya", regions=["Odisha", "All India"], rituals=["Pulling the chariot", "Darshan of deities", "Festival procession"], foods=["Mahaprasad (56 items)", "Khaja", "Enduri Pitha"]),
            FestivalDetail(name="Guru Purnima", month="July", duration_days=1, significance="Honoring spiritual teachers and the sage Vyasa", deity="Vyasa", tithi="Ashadha Purnima", regions=["All India"], rituals=["Guru worship", "Offering dakshina", "Vyasa Puja"], foods=["Special feast for guru", "Prasad"]),
            FestivalDetail(name="Nag Panchami", month="July/August", duration_days=1, significance="Worship of serpent deities", deity="Naga Devata", tithi="Shravana Shukla Panchami", regions=["All India"], rituals=["Snake worship", "Milk offering to snakes", "Drawing snake images"], foods=["Milk sweets", "Modak", "No cutting/frying food"]),
            FestivalDetail(name="Raksha Bandhan", month="August", duration_days=1, significance="Festival of sibling bond; sister ties protective thread on brother", deity="Vishnu", tithi="Shravana Purnima", regions=["All India"], rituals=["Rakhi tying", "Aarti", "Gift exchange"], foods=["Special sweets", "Barfi", "Laddoo", "Feast"]),
            FestivalDetail(name="Krishna Janmashtami", month="August", duration_days=2, significance="Birthday of Lord Krishna, eighth avatar of Vishnu", deity="Krishna", tithi="Bhadrapada Krishna Ashtami", regions=["All India"], rituals=["Midnight celebration", "Dahi Handi", "Fasting until midnight", "Cradle decoration"], foods=["Makhan Mishri", "Panjiri", "Panchamrit", "Charnamrit", "Kheer"]),
            FestivalDetail(name="Ganesh Chaturthi", month="August/September", duration_days=10, significance="Birthday of Lord Ganesha, remover of obstacles", deity="Ganesha", tithi="Bhadrapada Shukla Chaturthi", regions=["Maharashtra", "All India"], rituals=["Ganesh installation", "Daily puja", "Visarjan on day 10", "Modak offering"], foods=["Modak", "Ukadiche Modak", "Puran Poli", "Karanji"]),
            FestivalDetail(name="Onam", month="August/September", duration_days=10, significance="Kerala harvest festival celebrating King Mahabali's return", deity="Vamana (Vishnu)", tithi="Chingam month", regions=["Kerala"], rituals=["Pookalam (flower carpet)", "Vallamkali (boat race)", "Kaikottikali dance"], foods=["Onam Sadhya (26-course meal)", "Payasam", "Avial", "Olan", "Rasam"]),
            FestivalDetail(name="Hartalika Teej", month="August/September", duration_days=1, significance="Parvati's devotion to Shiva; festival for married women", deity="Parvati", tithi="Bhadrapada Shukla Tritiya", regions=["North India", "Maharashtra"], rituals=["Strict fasting", "Sand idol of Shiva-Parvati", "Night vigil"], foods=["Ghewar", "Malpua", "Fruits (after fast)"]),
            FestivalDetail(name="Navratri", month="September/October", duration_days=9, significance="Nine nights of Goddess worship - the nine forms of Durga", deity="Durga", tithi="Ashvina Shukla Pratipada to Navami", regions=["All India"], rituals=["Ghatasthapana", "Garba/Dandiya", "Durga Puja", "Kanya Pujan"], foods=["Sabudana Khichdi", "Kuttu ki puri", "Singhare ka atta", "Rajgira halwa"]),
            FestivalDetail(name="Durga Puja", month="September/October", duration_days=5, significance="Bengal's biggest festival celebrating Durga's victory over Mahishasura", deity="Durga", tithi="Shashthi to Dashami", regions=["West Bengal", "Odisha", "Assam", "Tripura"], rituals=["Pandal hopping", "Dhunuchi dance", "Sindoor khela", "Immersion"], foods=["Luchi-Alur Dom", "Kosha Mangsho", "Mishti Doi", "Sandesh", "Bhog khichuri"]),
            FestivalDetail(name="Dussehra", month="October", duration_days=1, significance="Victory of Rama over Ravana; Durga's victory over Mahishasura", deity="Rama/Durga", tithi="Ashvina Shukla Dashami", regions=["All India"], rituals=["Ravana effigy burning", "Shami Puja", "Weapon worship", "Vijayadashami procession"], foods=["Jalebi-Fafda (Gujarat)", "Special feast"]),
            FestivalDetail(name="Karva Chauth", month="October", duration_days=1, significance="Married women fast for husbands' long life", deity="Shiva-Parvati", tithi="Kartika Krishna Chaturthi", regions=["North India"], rituals=["Day-long fast", "Moon sighting", "Puja thali", "Breaking fast seeing husband through sieve"], foods=["Sargi (pre-dawn meal)", "Special dinner after moonrise"]),
            FestivalDetail(name="Diwali", month="October/November", duration_days=5, significance="Festival of lights - victory of light over darkness, Rama's return to Ayodhya", deity="Lakshmi/Ganesha", tithi="Kartika Amavasya", regions=["All India"], rituals=["Lakshmi-Ganesh Puja", "Diya lighting", "Fireworks", "Rangoli", "New clothes", "Gift exchange"], foods=["Kaju katli", "Gulab jamun", "Chakli", "Sev", "Anarsa", "Karanji"], greetings=["Happy Diwali", "Shubh Deepavali"]),
            FestivalDetail(name="Govardhan Puja", month="October/November", duration_days=1, significance="Krishna lifting Govardhan hill to protect villagers from Indra", deity="Krishna", tithi="Kartika Shukla Pratipada", regions=["North India", "Gujarat"], rituals=["Annakut offering", "Govardhan hill replica"], foods=["Annakut (56 food items)", "Chappan Bhog"]),
            FestivalDetail(name="Bhai Dooj", month="October/November", duration_days=1, significance="Sisters pray for brothers' well-being; celebration of sibling love", deity="Yama/Yamuna", tithi="Kartika Shukla Dwitiya", regions=["All India"], rituals=["Tilak on brother's forehead", "Aarti", "Gift exchange"], foods=["Sweets", "Special meal"]),
            FestivalDetail(name="Chhath Puja", month="October/November", duration_days=4, significance="Ancient Vedic festival of Sun worship", deity="Surya", tithi="Kartika Shukla Shashthi", regions=["Bihar", "Jharkhand", "UP", "Delhi"], rituals=["Holy bathing", "36-hour fast", "Standing in water offering to Sun"], foods=["Thekua", "Khasta", "Fruits"]),
            FestivalDetail(name="Tulsi Vivah", month="November", duration_days=1, significance="Ceremonial marriage of Tulsi plant to Lord Vishnu/Shaligram", deity="Vishnu/Tulsi", tithi="Kartika Shukla Ekadashi", regions=["Maharashtra", "North India"], rituals=["Tulsi plant decorated as bride", "Marriage ceremony", "Sugarcane mandap"], foods=["Til laddoo", "Ber", "Sugarcane"]),
            FestivalDetail(name="Skanda Sashti", month="November", duration_days=6, significance="Victory of Lord Murugan over demon Soorapadman", deity="Kartikeya/Murugan", tithi="Kartika Shukla Shashthi", regions=["Tamil Nadu", "Kerala", "Karnataka"], rituals=["Skanda Sashti Kavacham chanting", "Fasting", "Temple worship"], foods=["Fruits", "Kozhukattai", "Sundal"]),
            FestivalDetail(name="Gita Jayanti", month="December", duration_days=1, significance="Day when Krishna spoke the Bhagavad Gita to Arjuna", deity="Krishna", tithi="Margashirsha Shukla Ekadashi", regions=["All India"], rituals=["Gita recitation", "Gita Yajna", "Spiritual discourses"], foods=["Prasad", "Ekadashi foods"]),
            FestivalDetail(name="Vaikuntha Ekadashi", month="December/January", duration_days=1, significance="Most sacred Ekadashi; gates of Vaikuntha (Vishnu's abode) open", deity="Vishnu", tithi="Margashirsha Shukla Ekadashi", regions=["South India", "All India"], rituals=["Fasting", "Night vigil", "Vishnu Sahasranama", "Temple queue for Vaikuntha Dwaram"], foods=["Sabudana", "Fruits", "Non-grain foods"]),
            FestivalDetail(name="Mauni Amavasya", month="January/February", significance="Day of silence and holy bath at Triveni Sangam", deity="Multiple", tithi="Magha Amavasya", regions=["North India"], rituals=["Holy bath at Sangam", "Day of silence", "Charity"], foods=["Til products", "Khichdi"]),
            FestivalDetail(name="Holashtak", month="March", significance="Eight days before Holi; considered inauspicious for new beginnings", deity="Multiple", tithi="8 days before Holi", regions=["North India"], rituals=["No auspicious ceremonies", "Holi preparations"], foods=["Normal meals"]),
        ]

    def get_all_festivals(self) -> list[FestivalDetail]:
        return self._festivals

    def get_festival(self, name: str) -> FestivalDetail | None:
        for f in self._festivals:
            if name.lower() in f.name.lower():
                return f
        return None

    def get_festivals_by_month(self, month: str) -> list[FestivalDetail]:
        m = month.lower()
        return [f for f in self._festivals if m in f.month.lower()]

    def get_festivals_by_deity(self, deity: str) -> list[FestivalDetail]:
        d = deity.lower()
        return [f for f in self._festivals if d in f.deity.lower()]

    def get_festivals_by_region(self, region: str) -> list[FestivalDetail]:
        r = region.lower()
        return [f for f in self._festivals if any(r in reg.lower() for reg in f.regions)]

    def search_festivals(self, query: str) -> list[FestivalDetail]:
        q = query.lower()
        return [f for f in self._festivals if q in f.name.lower() or q in f.significance.lower()]
