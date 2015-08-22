model_features = [
 'city',
 'state',
 'hours_Thursday',
 'hours_Tuesday',
 'hours_Friday',
 'hours_Wednesday',
 'hours_Monday',
 'hours_Sunday',
 'hours_Saturday',
 'attributes_Accepts Credit Cards',
 'attributes_Good For Groups',
 'attributes_Price Range',
 'attributes_Alcohol',
 'attributes_Noise Level',
 'attributes_Waiter Service',
 'attributes_Wi-Fi',
 'attributes_Good For_latenight', # determined
 'attributes_Has TV',
 'attributes_Open 24 Hours',	# determined
 'attributes_Drive-Thru',
 'Turkish',
 'Asian Fusion',
 'Cupcakes',
 'Chicken Wings',
 'Salvadoran',
 'Vietnamese',
 'Fish & Chips',
 'Italian',
 'Scottish',
 'Middle Eastern',
 'Champagne Bars',
 'Breakfast & Brunch',
 'Spanish',
 'Indian',
 'Food Stands',
 'Sandwiches',
 'Latin American',
 'Brazilian',
 'Cheesestreaks',
 'Korean',
 'Canadian (New)',
 'Pizza',
 'Tea Rooms',
 'Desserts',
 'Dim Sum',
 'American (New)',
 'Pubs',
 'Tapas Bars',
 'Szechuan',
 'Fast Food',
 'Sushi Bars',
 'Thai',
 'Russian',
 'Persian/Iranian',
 'Barbeque',
 'Ramen',
 'Seafood',
 'Bistros',
 'Cuban',
 'Cafes',
 'Ethnic Food',
 'Wine Bars',
 'Salad',
 'Gelato',
 'Vegetarian',
 'Juiece Bars & Smoothies',
 'British',
 'Greek',
 'Lebanese',
 'Food',
 'African',
 'Cocktail Bars',
 'Comfort Food',
 'Dive Bars',
 'Bagels',
 'Restaurants',
 'Ice Cream & Frozen Yogurt',
 'Portuguese',
 'Steakhouses',
 'Mexican',
 'Chinese',
 'Burgers',
 'German',
 'Taiwanese',
 'Japanese',
 'Food Trucks',
 'Peruvian',
 'Mongolian',
 'Hot Dogs',
 'Cantonese',
 'Soul Food',
 'nearbyCounts']

food_categories = [
 'Turkish',
 'Asian Fusion',
 'Cupcakes',
 'Chicken Wings',
 'Salvadoran',
 'Vietnamese',
 'Fish & Chips',
 'Italian',
 'Scottish',
 'Middle Eastern',
 'Champagne Bars',
 'Breakfast & Brunch',
 'Spanish',
 'Indian',
 'Food Stands',
 'Sandwiches',
 'Latin American',
 'Brazilian',
 'Cheesestreaks',
 'Korean',
 'Canadian (New)',
 'Pizza',
 'Tea Rooms',
 'Desserts',
 'Dim Sum',
 'American (New)',
 'Pubs',
 'Tapas Bars',
 'Szechuan',
 'Fast Food',
 'Sushi Bars',
 'Thai',
 'Russian',
 'Persian/Iranian',
 'Barbeque',
 'Ramen',
 'Seafood',
 'Bistros',
 'Cuban',
 'Cafes',
 'Ethnic Food',
 'Wine Bars',
 'Salad',
 'Gelato',
 'Vegetarian',
 'Juiece Bars & Smoothies',
 'British',
 'Greek',
 'Lebanese',
 'Food',
 'African',
 'Cocktail Bars',
 'Comfort Food',
 'Dive Bars',
 'Bagels',
 'Restaurants',
 'Ice Cream & Frozen Yogurt',
 'Portuguese',
 'Steakhouses',
 'Mexican',
 'Chinese',
 'Burgers',
 'German',
 'Taiwanese',
 'Japanese',
 'Food Trucks',
 'Peruvian',
 'Mongolian',
 'Hot Dogs',
 'Cantonese',
 'Soul Food'
]

alcoholMap = {
	"full_bar":2,
    "beer_and_wine":1,
    "none":0}


noiseMap = {"quiet":0,
            "average":1,
            "loud":2,
            "very_loud":3}


wifiMap = {	"no":0,
           	"free":1,
           	"paid":2}

priceRangeMap = {}

stateMap = {	
	 'AZ': 5,
	 'BW': 11,
	 'EDH': 9,
	 'IL': 4,
	 'MLN': 10,
	 'NC': 1,
	 'NV': 6,
	 'ON': 8,
	 'PA': 0,
	 'QC': 7,
	 'SC': 2,
	 'WI': 3}

stateToAbbr = {
	'Alabama': 'AL',
	'Alaska': 'AK',
	'American Samoa': 'AS',
	'Arizona': 'AZ',
	'Arkansas': 'AR',
	'California': 'CA',
	'Colorado': 'CO',
	'Connecticut': 'CT',
	'Delaware': 'DE',
	'Dist. of Columbia': 'DC',
	'Florida': 'FL',
	'Georgia': 'GA',
	'Guam': 'GU',
	'Hawaii': 'HI',
	'Idaho': 'ID',
	'Illinois': 'IL',
	'Indiana': 'IN',
	'Iowa': 'IA',
	'Kansas': 'KS',
	'Kentucky': 'KY',
	'Louisiana': 'LA',
	'Maine': 'ME',
	'Maryland': 'MD',
	'Marshall Islands': 'MH',
	'Massachusetts': 'MA',
	'Michigan': 'MI',
	'Micronesia': 'FM',
	'Minnesota': 'MN',
	'Mississippi': 'MS',
	'Missouri': 'MO',
	'Montana': 'MT',
	'Nebraska': 'NE',
	'Nevada': 'NV',
	'New Hampshire': 'NH',
	'New Jersey': 'NJ',
	'New Mexico': 'NM',
	'New York': 'NY',
	'North Carolina': 'NC',
	'North Dakota': 'ND',
	'Northern Marianas': 'MP',
	'Ohio': 'OH',
	'Oklahoma': 'OK',
	'Oregon': 'OR',
	'Palau': 'PW',
	'Pennsylvania': 'PA',
	'Puerto Rico': 'PR',
	'Rhode Island': 'RI',
	'South Carolina': 'SC',
	'South Dakota': 'SD',
	'Tennessee': 'TN',
	'Texas': 'TX',
	'Utah': 'UT',
	'Vermont': 'VT',
	'Virginia': 'VA',
	'Virgin Islands': 'VI',
	'Washington': 'WA',
	'West Virginia': 'WV',
	'Wisconsin': 'WI',
	'Wyoming': 'WY'
}

cityMap = {	 
	 'Ahwatukee': 38,
	 'lentown': 206,
	 'Anjou': 110,
	 'Anthem': 40,
	 'Apache Junction': 44,
	 'Arlington': 265,
	 'Aspinwall': 69,
	 'Avondale': 88,
	 'Baden-Baden': 258,
	 "Baie-D'urfe": 135,
	 'Balerno': 218,
	 'Bapchule': 84,
	 'Beaconsfield': 179,
	 'Bellevue': 11,
	 'Bellvue': 10,
	 'Belmont': 16,
	 'Bietigheim': 191,
	 'Black Canyon City': 54,
	 'Blainville': 144,
	 'Bloomfield': 238,
	 'Boisbriand': 143,
	 'Bonnyrigg and Lasswade': 220,
	 'Boucherville': 163,
	 'Boulder City': 97,
	 'Braddock': 0,
	 'Brentwood': 200,
	 'Bridgeville': 154,
	 'Brossard': 136,
	 'Buckeye': 55,
	 'Cambridge': 149,
	 'Carefree': 96,
	 'Carnegie': 1,
	 'Casa Grande': 45,
	 'Castle Shannon': 14,
	 'Cave Creek': 82,
	 'Central City Village': 253,
	 'Centropolis Laval': 270,
	 'Champaign': 32,
	 'Chandler': 42,
	 'Charlotte': 20,
	 'Chateau': 241,
	 'Chomedey': 235,
	 'City of Edinburgh': 248,
	 'Clark County': 252,
	 'Clover': 23,
	 'Columbus': 173,
	 'Communaut\xc3\xa9-Urbaine-de-Montr\xc3\xa9al': 221,
	 'Concord': 73,
	 'Concord Mills': 203,
	 'Conestogo': 210,
	 'Coolidge': 46,
	 'Cote-Saint-Luc': 194,
	 'Cote-des-Neiges-Notre-Dame-de-Grace': 228,
	 'Cottage Grove': 77,
	 'Crafton': 72,
	 'Cramond Bridge': 231,
	 'Dalkeith': 153,
	 'Dane': 78,
	 'De Forest': 24,
	 'DeForest': 106,
	 'Delmont': 15,
	 'Deux-Montagnes Regional County Municipality': 232,
	 'Dollard-Des Ormeaux': 269,
	 'Dollard-Des-Ormeaux': 127,
	 'Dollard-des-Ormeaux': 150,
	 'Dormont': 180,
	 'Dorval': 130,
	 'Downtown': 240,
	 'Dravosburg': 175,
	 'Durmersheim': 184,
	 'Edinburgh': 151,
	 'Eggenstein-Leopoldshafen': 185,
	 'El Mirage': 90,
	 'Enterprise': 168,
	 'Ettlingen': 183,
	 'Fabreville': 123,
	 'Fitchburg': 79,
	 'Florence': 47,
	 'Fort Kinnaird': 237,
	 'Fort McDowell': 107,
	 'Fort Mcdowell': 223,
	 'Fort Mill': 21,
	 'Fountain Hills': 52,
	 'Gila Bend': 91,
	 'Gilbert': 48,
	 'Glendale': 36,
	 'Glendale Az': 214,
	 'Gold Canyon': 43,
	 'Goodyear': 56,
	 'Green Tree': 160,
	 'Greenfield Park': 137,
	 'Guadalupe': 87,
	 'Harrisburg': 74,
	 'Heidelberg': 230,
	 'Henderson': 62,
	 'Henderson (Green  Valley)': 268,
	 'Henderson (Stephanie)': 267,
	 'Henderson and Las vegas': 222,
	 'Higley': 101,
	 'Homestead': 3,
	 'Huntersville': 104,
	 'Indian Land': 199,
	 'Indian Trail': 75,
	 'Juniper Green': 157,
	 'Karlsbad': 186,
	 'Karlsruhe': 187,
	 'Kirkland': 132,
	 'Kitchener': 146,
	 "L'\xc3\x8ele-Bizard": 208,
	 "L'\xc3\x8ele-des-Soeurs": 250,
	 'La Prairie': 141,
	 'LaSalle': 201,
	 'Lachine': 125,
	 'Lake Wylie': 22,
	 'Las Vegas': 64,
	 'Las Vegas ': 103,
	 'Lasalle': 126,
	 'Lasswade': 155,
	 'Laval': 122,
	 'Laveen': 92,
	 'Lawrenceville': 245,
	 'Litchfield Park': 57,
	 'Loanhead': 251,
	 'Longueuil': 139,
	 'Lower Lawrenceville': 242,
	 'Madison': 29,
	 'Maricopa': 85,
	 'Mascouche': 259,
	 'Matthews': 17,
	 'Mc Farland': 25,
	 'Mc Kees Rocks': 174,
	 'McFarland': 172,
	 'McKees Rocks': 9,
	 'McKeesport': 8,
	 'Mcfarland': 263,
	 'Mckees Rocks': 71,
	 'Mesa': 41,
	 'Middleton': 26,
	 'Millvale': 225,
	 'Mint Hill': 76,
	 'Monona': 30,
	 'Mont-Royal': 119,
	 'Montreal': 108,
	 'Montreal-Est': 117,
	 'Montreal-Nord': 219,
	 'Montreal-Ouest': 121,
	 'Montreal-West': 261,
	 'Montr\xc3\xa9al': 109,
	 'Montr\xc3\xa9al-Nord': 112,
	 'Montr\xc3\xa9al-Ouest': 205,
	 'Mont\xc3\xa9al': 116,
	 'Morristown': 102,
	 'Mount Holly': 18,
	 'Mount Lebanon': 12,
	 'Mount Royal': 246,
	 'Mount Washington': 67,
	 'Mt Lebanon': 271,
	 'Mt. Oliver Boro': 169,
	 'Munhall': 4,
	 'Musselburgh': 217,
	 'N Las Vegas': 98,
	 'N. Las Vegas': 65,
	 'NELLIS AFB': 226,
	 'Nellis AFB': 233,
	 'Nellis Afb': 165,
	 'New Dundee': 202,
	 'New River': 83,
	 'New Town': 255,
	 'Newbridge': 156,
	 'North Las Vegas': 63,
	 'North Scottsdale': 99,
	 'Oakland': 105,
	 'Old Town': 262,
	 'Outremont': 114,
	 'PHOENIX': 236,
	 'Paradise': 167,
	 'Paradise Valley': 37,
	 'Peoria': 53,
	 'Pfinztal': 188,
	 'Pheonix': 207,
	 'Phoenix': 34,
	 'Phoenix Sky Harbor Center': 244,
	 'Phoenix-Ahwatukee': 39,
	 'Pierrefonds': 128,
	 'Pineville': 19,
	 'Pittsburgh': 2,
	 'Pittsburgh/S. Hills Galleria': 176,
	 'Pittsburgh/Waterfront': 6,
	 'Pittsburrgh': 204,
	 'Pointe-Aux-Trembles': 113,
	 'Pointe-Claire': 131,
	 'Quebec': 216,
	 'Queen Creek': 49,
	 'Queensferry': 181,
	 'Ratho': 158,
	 'Rheinstetten': 182,
	 'Rio Verde': 86,
	 'Rock Hill': 239,
	 'Rosemere': 145,
	 'Rosem\xc3\xa8re': 209,
	 'Roxboro': 129,
	 'Saguaro Lake': 178,
	 'Saint Jacobs': 177,
	 'Saint Laurent': 213,
	 'Saint-Eustache': 215,
	 'Saint-Hubert': 138,
	 'Saint-Lambert': 140,
	 'Saint-Laurent': 120,
	 'Saint-Leonard': 111,
	 'Sainte-Ann-De-Bellevue': 196,
	 'Sainte-Anne-De-Bellevue': 133,
	 'Sainte-Anne-de-Bellevue': 229,
	 'Sainte-Genevieve': 134,
	 'Sainte-Therese': 142,
	 'Sainte-Th\xc3\xa9r\xc3\xa8se': 211,
	 'San Tan Valley': 161,
	 'Savoy': 33,
	 'Scotland': 256,
	 'Scottsdale': 35,
	 'Scottsdale Country Acres': 257,
	 'Sedona': 61,
	 'Sharpsburg': 68,
	 'South Gyle': 249,
	 'South Queensferry': 152,
	 'Spring Valley': 166,
	 'St Clements': 147,
	 'St Jacobs': 159,
	 'St. Jacobs': 260,
	 'Stallings': 162,
	 'Ste-Rose': 224,
	 'Stockbridge': 247,
	 'Stoughton': 80,
	 'Stowe Township': 266,
	 'Stutensee': 193,
	 'Stutensee neuthard': 234,
	 'Summerlin': 100,
	 'Sun City': 89,
	 'Sun City West': 95,
	 'Sun Lakes': 50,
	 'Sun Prairie': 27,
	 'Surprise': 59,
	 'Surprise Crossing': 227,
	 'Swissvale': 13,
	 'Tega Cay': 171,
	 'Tempe': 51,
	 'Terrebonne': 212,
	 'Tolleson': 93,
	 'Tonopah': 58,
	 'Tonto Basin': 164,
	 'Tortilla Flat': 170,
	 'Urbana': 31,
	 'Verdun': 115,
	 'Verona': 66,
	 'Victoria Park': 198,
	 'Vimont': 124,
	 'Waldbronn': 190,
	 'Waterloo': 148,
	 'Waunakee': 81,
	 'Waxhaw': 264,
	 'Weddington': 254,
	 'Weingarten': 189,
	 'Weingarten (Baden)': 192,
	 'Wesley Chapel': 195,
	 'West Homestead': 5,
	 'West Mifflin': 7,
	 'Westmount': 118,
	 'Whitehall': 243,
	 'Wickenburg': 60,
	 'Wilkinsburg': 70,
	 'Windsor': 28,
	 'Woolwich': 197,
	 'Youngtown': 94}