"""RegionalVariations showing how festivals differ across India."""
from __future__ import annotations
from ..models import RegionalVariation


class RegionalVariations:
    """Database of how festivals are celebrated differently across Indian regions."""

    def __init__(self) -> None:
        self._variations: list[RegionalVariation] = self._load_variations()

    def _load_variations(self) -> list[RegionalVariation]:
        return [
            # Makar Sankranti variations
            RegionalVariation(festival_name="Makar Sankranti", region="Maharashtra", local_name="Makar Sankranti", special_customs="Married women exchange til-gul and haldi-kumkum. Kite flying.", special_foods=["Til gul laddoo", "Puran Poli", "Bajra roti"]),
            RegionalVariation(festival_name="Makar Sankranti", region="Gujarat", local_name="Uttarayan", special_customs="International kite festival. Undhiyu feast.", special_foods=["Undhiyu", "Jalebi", "Chikki"]),
            RegionalVariation(festival_name="Makar Sankranti", region="Punjab", local_name="Maghi", special_customs="Holy bath, kheer-roti feast. Celebrated day after Lohri.", special_foods=["Kheer", "Makki di roti", "Sarson da saag"]),
            RegionalVariation(festival_name="Makar Sankranti", region="Assam", local_name="Magh Bihu", special_customs="Community feast (Bhogali Bihu). Meji bonfire.", special_foods=["Til pitha", "Laru", "Sunga pitha"]),
            RegionalVariation(festival_name="Makar Sankranti", region="Tamil Nadu", local_name="Pongal", special_customs="Four-day celebration. Cattle decoration (Jallikattu). Kolam.", special_foods=["Sweet Pongal", "Ven Pongal", "Vadai", "Payasam"]),

            # Holi variations
            RegionalVariation(festival_name="Holi", region="Mathura-Vrindavan", local_name="Lathmar Holi", special_customs="Women playfully beat men with sticks. Week-long celebration.", special_foods=["Gujiya", "Thandai", "Malpua"]),
            RegionalVariation(festival_name="Holi", region="Bengal", local_name="Dol Jatra", special_customs="Radha-Krishna procession. Abir (dry colors) used. Cultural programs.", special_foods=["Malpua", "Sandesh", "Basanti Pulao"]),
            RegionalVariation(festival_name="Holi", region="Rajasthan", local_name="Royal Holi", special_customs="Elephant festival in Jaipur. Royal processions.", special_foods=["Gujiya", "Dahi Bhalle", "Dal Baati"]),
            RegionalVariation(festival_name="Holi", region="South India", local_name="Kamadahana", special_customs="Burning of Kama effigy. Less color play, more religious.", special_foods=["Obbattu", "Payasam"]),

            # Navratri/Durga Puja variations
            RegionalVariation(festival_name="Navratri", region="Gujarat", local_name="Navratri", special_customs="Nine nights of Garba and Dandiya Raas. Largest dance festival.", special_foods=["Sabudana Khichdi", "Rajgira roti", "Fasting foods"]),
            RegionalVariation(festival_name="Navratri", region="West Bengal", local_name="Durga Puja", special_customs="Elaborate pandals. Dhunuchi dance. Sindoor khela. Cultural programs.", special_foods=["Luchi", "Alur Dom", "Bhog Khichuri", "Mishti"]),
            RegionalVariation(festival_name="Navratri", region="South India", local_name="Golu/Bommai Kolu", special_customs="Doll display on steps. Women visit each others' Golu.", special_foods=["Sundal", "Payasam", "Kozhukattai"]),
            RegionalVariation(festival_name="Navratri", region="North India", local_name="Navratri", special_customs="Fasting 9 days. Kanya Pujan. Ram Leela performances.", special_foods=["Kuttu puri", "Singhara atta", "Aloo sabzi"]),

            # Diwali variations
            RegionalVariation(festival_name="Diwali", region="North India", local_name="Diwali", special_customs="5-day celebration: Dhanteras, Naraka Chaturdashi, Diwali, Govardhan, Bhai Dooj.", special_foods=["Kaju Katli", "Gulab Jamun", "Sev", "Chakli"]),
            RegionalVariation(festival_name="Diwali", region="West Bengal", local_name="Kali Puja", special_customs="Goddess Kali worshipped instead of Lakshmi. Tantric rituals.", special_foods=["Naru", "Sandesh", "Luchi"]),
            RegionalVariation(festival_name="Diwali", region="South India", local_name="Naraka Chaturdashi", special_customs="Oil bath at dawn. Krishna's victory over Narakasura.", special_foods=["Murukku", "Laddu", "Mixture"]),
            RegionalVariation(festival_name="Diwali", region="Gujarat", local_name="New Year (Bestu Varas)", special_customs="Business new year. New account books. Chopda Pujan.", special_foods=["Mohanthal", "Ghughra", "Dry fruit sweets"]),

            # Ganesh Chaturthi variations
            RegionalVariation(festival_name="Ganesh Chaturthi", region="Maharashtra", local_name="Ganeshotsav", special_customs="10-day public celebration. Sarvajanik mandals. Visarjan procession.", special_foods=["Ukadiche Modak", "Puran Poli", "Karanji"]),
            RegionalVariation(festival_name="Ganesh Chaturthi", region="Andhra/Telangana", local_name="Vinayaka Chavithi", special_customs="21 types of patri (leaves) offered. Clay Ganesha.", special_foods=["Modak", "Kudumulu", "Undrallu"]),
            RegionalVariation(festival_name="Ganesh Chaturthi", region="Tamil Nadu", local_name="Vinayagar Chaturthi", special_customs="Kozhukattai offering. Eco-friendly celebrations.", special_foods=["Kozhukattai", "Modak", "Sundal"]),

            # Krishna Janmashtami variations
            RegionalVariation(festival_name="Krishna Janmashtami", region="Maharashtra", local_name="Dahi Handi", special_customs="Human pyramid to break pot of butter hung high.", special_foods=["Makhan", "Panchamrit", "Kheer"]),
            RegionalVariation(festival_name="Krishna Janmashtami", region="Mathura-Vrindavan", local_name="Janmashtami", special_customs="Grand midnight celebration. Rasleela dramas.", special_foods=["Makhan Mishri", "Panjiri", "56 bhog"]),
        ]

    def get_variations(self, festival_name: str) -> list[RegionalVariation]:
        return [v for v in self._variations if festival_name.lower() in v.festival_name.lower()]

    def get_by_region(self, region: str) -> list[RegionalVariation]:
        r = region.lower()
        return [v for v in self._variations if r in v.region.lower()]

    def get_all(self) -> list[RegionalVariation]:
        return self._variations
