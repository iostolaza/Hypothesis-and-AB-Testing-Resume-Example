import pandas as pd
import numpy as np
import random

#Provided list of Job Titles
job_titles = [
    "Account Executive", "Account Manager", "Administrative Assistant", "Assistant Manager", "Branch Manager",
    "Business Analyst", "Business Development Manager", "Chief Executive Officer (CEO)", "Chief Financial Officer (CFO)",
    "Chief Operating Officer (COO)", "Chief Technology Officer (CTO)", "Client Services Manager", "Content Manager",
    "Copywriter", "Customer Service Representative", "Data Analyst", "Data Scientist", "Digital Marketing Manager",
    "Director of Marketing", "Director of Sales", "Event Manager", "Executive Assistant", "Finance Manager",
    "Financial Analyst", "General Manager", "Graphic Designer", "Human Resources Manager", "IT Manager",
    "Legal Assistant", "Marketing Coordinator", "Marketing Manager", "Media Buyer", "Office Manager", "Operations Manager",
    "Product Manager", "Project Coordinator", "Project Manager", "Public Relations Specialist", "Receptionist",
    "Recruiter", "Research Assistant", "Sales Associate", "Sales Director", "Sales Manager", "Software Developer",
    "Software Engineer", "Technical Support Specialist", "UX Designer", "Web Developer", "Accountant", "Auditor",
    "Budget Analyst", "Compliance Officer", "Controller", "Cost Estimator", "Credit Analyst", "Economist",
    "Financial Examiner", "Loan Officer", "Management Analyst", "Market Research Analyst", "Personal Financial Advisor",
    "Purchasing Manager", "Tax Examiner", "Training and Development Manager", "Compensation and Benefits Manager",
    "Human Resources Specialist", "Labor Relations Specialist", "Employment, Recruitment, and Placement Specialist",
    "Meeting, Convention, and Event Planner", "Fundraiser", "Public Relations Manager", "Advertising Sales Agent",
    "Art Director", "Editor", "Film and Video Editor", "Graphic Designer", "Multimedia Artist and Animator",
    "Photographer", "Producer and Director", "Public Relations Specialist", "Writer and Author", "Medical and Health Services Manager",
    "Medical Records and Health Information Technician", "Occupational Health and Safety Specialist", "Optician",
    "Pharmacist", "Pharmacy Technician", "Physical Therapist", "Physician Assistant", "Radiologic Technologist",
    "Registered Nurse", "Respiratory Therapist", "Speech-Language Pathologist", "Surgeon", "Veterinary Technician",
    "Agricultural and Food Scientist", "Anthropologist", "Archaeologist", "Atmospheric Scientist", "Biochemist",
    "Biophysicist", "Chemist", "Conservation Scientist", "Environmental Scientist", "Forester", "Geographer",
    "Geoscientist", "Hydrologist", "Microbiologist", "Medical Scientist", "Physicist", "Political Scientist",
    "Psychologist", "Sociologist", "Survey Researcher", "Urban and Regional Planner", "Zoologist",
    "Aerospace Engineer", "Biomedical Engineer", "Chemical Engineer", "Civil Engineer", "Computer Hardware Engineer",
    "Electrical Engineer", "Electronics Engineer", "Environmental Engineer", "Health and Safety Engineer", "Industrial Engineer",
    "Materials Engineer", "Mechanical Engineer", "Mining and Geological Engineer", "Nuclear Engineer", "Petroleum Engineer",
    "Sales Engineer", "Transportation Engineer", "Agricultural Engineer", "Architect", "Surveyor",
    "Biomedical Equipment Technician", "Computer Programmer", "Database Administrator", "Information Security Analyst",
    "Network and Computer Systems Administrator", "Software Developer", "Systems Analyst", "Web Developer",
    "Construction Manager", "Cost Estimator", "Electrician", "Plumber", "Solar Photovoltaic Installer",
    "Wind Turbine Technician", "Barista", "Bartender", "Chef", "Cook", "Food Preparation Worker",
    "Food Server", "Host or Hostess", "Restaurant Manager", "Waiter or Waitress", "Childcare Worker",
    "Nanny", "Personal Care Aide", "Recreation Worker", "Rehabilitation Counselor", "Residential Advisor",
    "Social Worker", "Teacher Assistant", "Fitness Trainer", "Group Fitness Instructor", "Massage Therapist",
    "Recreation and Fitness Studies Teacher", "Athletic Trainer", "Choreographer", "Dancer", "Actor",
    "Announcer", "Broadcast and Sound Engineering Technician", "Camera Operator", "Editor", "Film and Video Editor",
    "Music Director", "Musician", "Producer and Director", "Reporter", "Correspondent", "Writer and Author"
]
#print(job_titles[:10])

#Provided list of full names
names = [
    "Bethany Schroeder", "Izaiah Combs", "Irene Roberson", "Shepherd Leon", "Amora Walton", "Dominick Pineda",
    "Nola Blackwell", "Marcellus Monroe", "Carly O’Donnell", "Lian Flores", "Emilia Odom", "Kylian Morales",
    "Skylar Mathews", "Jamir Hull", "Andi Rhodes", "Titus Armstrong", "Presley Bennett", "Leonardo Wilkerson",
    "Janiyah Dunlap", "Aries Maynard", "Carolyn Burgess", "Kolton Scott", "Aurora Harmon", "Roberto Poole",
    "Bonnie King", "Julian Huang", "Francesca Daugherty", "Turner Clay", "Aliana Prince", "Aron Holloway",
    "Mae Lawson", "Lane Terry", "Wren Villegas", "Clyde Gregory", "Alaya Salas", "Zaiden Cordova",
    "Florence Lucas", "Chance Hoffman", "Aspen Manning", "Seth Underwood", "Ensley Hughes", "Everett Randolph",
    "Kailey Graham", "Giovanni Lopez", "Gianna McLaughlin", "Ibrahim Leal", "Murphy Blankenship", "Ernesto Baker",
    "Isla Dudley", "Colter Goodman", "Carolina Valdez", "Kyler Shah", "Angelica Foster", "Kayden Savage",
    "Louise Doyle", "Kashton Hogan", "Kathryn Logan", "Rocco Fry", "Clarissa Camacho", "Tatum Miller",
    "Isabella Wall", "Issac Berger", "Laylah Holloway", "Sutton Lugo", "Kaylie Norris", "Cairo McMahon",
    "Belen Harmon", "Roberto Owen", "Mikayla Griffin", "Ayden Gentry", "Amelie Friedman", "Darwin Callahan",
    "Kimber Melton", "Lennon Stout", "Chana Stanton", "Zyair Castillo", "Eva Fleming", "Fernando Moody",
    "Elaine Scott", "Leo Cantrell", "Yamileth Bradford", "Ander Nunez", "Mya Higgins", "Sterling Warren",
    "Sloane Wang", "Cohen Cervantes", "Aylin Rice", "Graham Cantu", "Galilea Bonilla", "Aden Robinson",
    "Nora Walton", "Dominick Simmons", "Reagan Morton", "Roland Ryan", "Morgan White", "Aiden Everett",
    "Noah Ryan", "Timothy Velez", "Megan Spencer", "Ace Black", "Molly Hardy", "Jayceon Hess",
    "Kaliyah Davila", "Grey Baldwin", "Esmeralda Acevedo", "Dakari Hoover", "Virginia Lim", "Cal Livingston",
    "Milena Carr", "Kash Lucas", "Phoenix Landry", "Jaxx Boone", "Mariam Murray", "Ashton Sherman",
    "Addilyn Orr", "Benicio Ramirez", "Grace Keith", "Jagger Middleton", "Madalyn Solis", "Ronin Flores",
    "Emilia Hardy", "Jayceon Patton", "Lorelei Mathews", "Jamir Castaneda", "Keira Waller", "Marley Coffey",
    "Paola Clark", "John Weber", "Alayah Frazier", "Callum Dudley", "Hadleigh Aguirre", "Andy Shaffer",
    "Alanna Austin", "Omar Newton", "Braelynn Paul", "Noel Larsen", "Xiomara Patrick", "Derrick Gardner",
    "Jordyn Duarte", "Abdullah Burnett", "Emberly Walter", "Lochlan Wagner", "Maeve Henry", "Carlos Figueroa",
    "Lilith Moyer", "Ahmir Cline", "Lina Haynes", "Kason Mathis", "Anne Hunt", "Jesus Ramirez",
    "Grace Benton", "Jamal Tate", "Skye Perkins", "Kyrie Welch", "Amira Larsen", "Brycen Oliver",
    "Camille Colon", "Bruce Day", "Hayden Bailey", "Axel Galvan", "Dallas Leblanc", "Braden Richards",
    "Trinity Fields", "Clayton Duarte", "Kynlee Herrera", "River Grimes", "Braelyn Knapp", "Boden Roman",
    "Astrid Gill", "Matthias Durham", "Tiffany Moody", "Ryland Hoover", "Virginia Caldwell", "Rylan Delacruz",
    "Celine Munoz", "Justin Cochran", "Alma Camacho", "Tatum Bradshaw", "Berkley Roman", "Kian Hinton",
    "Jaelynn Salgado", "Trace Barnett", "Harlow McLaughlin", "Ibrahim Marsh", "Adelina Lin", "Conor Todd",
    "Zariah Carey", "Watson Cox", "Sadie Bentley", "Randy Shelton", "Makenzie Medrano", "Arian Bradshaw",
    "Berkley McCarty", "Blaise Berger", "Laylah Rogers", "Colton Melton", "Kamiyah Murphy", "Cameron McDaniel",
    "Dahlia Harding", "Brodie Fry", "Clarissa Gordon", "Karter Price", "Piper Stephenson", "Joe David",
    "Haylee Blake", "Zyaire Burch", "Freyja Casey", "Armando Roth", "Elliot Pearson", "Gunner Mills",
    "June Cunningham", "Alejandro Powers", "Michelle Knight", "Beckett Graves", "Elle York", "Leandro Berger",
    "Laylah Beil", "Ariel Gardner", "Jordyn Hensley", "Layne Finley", "Jovie Bartlett", "Kace Montgomery",
    "Evangeline Beard", "Nathanael Strong", "Margo Rice", "Graham Figueroa", "Lilith Sloan", "Ocean Bradford",
    "Rhea Walters", "Colson Hudson", "Kamila Montgomery", "Maximiliano Harrell", "Kara Herring", "Henrik Stephens",
    "Millie Landry", "Jaxx Villalobos", "Zoya Novak", "Bishop Reeves", "Lana Miller", "Benjamin Benson",
    "Collins Norris", "Cairo Nash", "Novah Johns", "Joziah Terrell", "Paityn Friedman", "Darwin Cano",
    "Egypt McLaughlin", "Ibrahim Avalos", "Paloma Davidson", "Dante James", "Quinn Barton", "Cassius Garrison",
    "Cadence Branch", "Keenan Holt", "Adelynn Cantrell", "Harris Delgado", "Alani Delgado", "Colt Nielsen",
    "Vienna Carrillo", "Wade Jaramillo", "Guadalupe Swanson", "Hugo Truong", "Judith Bryant", "Jonah O’Donnell",
    "Bellamy Guerrero", "Bryce Brock", "Jada Stewart", "Nolan Lawrence", "Lauren Burch", "Gerald Saunders",
    "Meadow Melendez", "Nikolas Archer", "Kadence Aguilar", "Milo Michael", "Aubriella Collier", "Edison Roach",
    "Lyanna Quintero", "Thatcher Hodges", "Eve Huerta", "Douglas McMahon", "Belen McIntyre", "Eliseo Brennan",
    "Elodie Berry", "Adonis Gill", "Jordan Ball", "Shane Nolan", "Itzayana Weber", "Crew Rush",
    "Maleah Ramos", "Angel Silva", "Lucia Tanner", "Bruno Clements", "Cara Stewart", "Nolan Andrews",
    "Payton Mahoney", "Kamryn Guerrero", "Margot Bailey", "Axel Valentine", "August Magana", "Rey McCullough",
    "Hana Cline", "Cullen Guevara", "Teresa Baldwin", "Jaiden Petersen", "Fernanda Cannon", "Archie McDaniel",
    "Dahlia Henderson", "Beau Campos", "Sutton Cuevas", "Brecken Robertson", "Harmony Hickman", "Jakobe Robles",
    "Felicity Banks", "Martin McBride", "Kelsey Lawrence", "Kaleb Brennan", "Elodie Williams", "Oliver Gallegos",
    "Ari Jordan", "Sawyer Rosario", "Louisa Beard", "Nathanael Shah", "Angelica Solomon", "Musa Blackburn",
    "Frida Krueger", "Jones Hartman", "Kennedi Rosas", "Remi Valenzuela", "Henley Boyd", "Dean Huffman",
    "Hayley Dudley", "Colter Meyers", "Leyla Jackson", "Sebastian Simon", "Kalani Horton", "Garrett McConnell",
    "Denise Parks", "Gianni Francis", "Daniella Sloan", "Ocean McDaniel", "Dahlia Harding", "Brodie Arnold",
    "Finley Marks", "Amos Andrews", "Payton Kerr", "Louie Quintana", "Kenia Kline", "Ramon Frederick",
    "Sariyah Townsend", "Alexis Wang", "Kailani Farley", "Graysen Santiago", "Nyla Ali", "Arjun Clark",
    "Chloe Hamilton", "Jason Ellison", "Raina Lucero", "Felipe Bush", "Everlee Mayer", "Yahir Brooks",
    "Autumn Rogers", "Colton Ramsey", "Lyric Butler", "Ryder Erickson", "Sabrina Ballard", "Kenzo Nelson",
    "Everly Hayden", "Leroy Avila", "Amiyah Randolph", "Eugene Cline", "Lina Meyers", "Julien Bryan",
    "Meredith Quintero", "Thatcher Griffith", "Alicia Leal", "Cedric Camacho", "Armani Floyd", "Pierce Martin",
    "Mila Day", "Kayson Vaughan", "Nancy Sims", "Brian Bryant", "Parker McConnell", "London Todd",
    "Zariah Sparks", "Drake Shannon", "Harlee Le", "Damien Ward", "Ariana Rosario", "Jedidiah Cannon",
    "Noa Luna", "Erick Estrada", "Sawyer Espinosa", "Khalid Johnson", "Emma Vasquez", "Rowan Castillo",
    "Eva Hernandez", "Mason Woodward", "Drew Person", "Moses Cortes", "Lea Reyes", "Eli Richmond",
    "Whitney Warren", "Abel Watts", "Melissa Mitchell", "Jaxon Gonzalez", "Abigail Long", "Jace Phelps",
    "Laney Russell", "Weston Colon", "Remy Murphy", "Cameron Vasquez", "Rose Riley", "Amari Cantu",
    "Galilea Branch", "Keenan Stone", "Catalina Peck", "Yousef Bentley", "Jaylin Harvey", "Cayden Buck",
    "Livia Pennington", "Bobby Garcia", "Amelia Curry", "Briggs Carey", "Alora Mitchell", "Jaxon Cannon",
    "Noa Buck", "Jon Whitaker", "Ivanna Sanders", "Jose Holt", "Adelynn Cobb", "Raphael Flores",
    "Emilia Murillo", "Lance Carpenter", "Lilly Suarez", "Soren Montoya", "Kamryn Horton", "Garrett Hensley",
    "Malaya Le", "Damien Chambers", "Makayla Rosario", "Jedidiah Velez", "Megan Morse", "Bode Jackson",
    "Avery Drake", "Jalen Schmidt", "Kimberly Kane", "Brock Macdonald", "Rosalia Stuart", "Dion Jordan",
    "Adalynn Hopkins", "Ali Zhang", "Sarai Howe", "Alaric Mueller", "Imani Burke", "Jax Correa",
    "Valery Palacios", "Thaddeus Yates", "Charley Vega", "Aidan McGuire", "April Blair", "Troy Villegas",
    "Jessie Andrews", "Lukas Dunn", "Olive Chambers", "Orion Pittman", "Marie Boyle", "Robin Harrison",
    "Jasmine Padilla", "Jaden York", "Milan Bauer", "Kieran Sullivan", "Melanie Robbins", "Finnegan Horne",
    "Marlowe Valencia", "Dax Boone", "Mariam Mata", "Ray Burke", "Vera Griffin", "Ayden Thomas",
    "Elizabeth Zamora", "Quentin Glass", "Clare Randolph", "Eugene Correa", "Valery Griffith", "Franklin Cisneros",
    "Janelle McDaniel", "Major Buckley", "Theodora Curry", "Briggs Hail", "Lainey Henson", "Bellamy Dominguez",
    "Raegan Ingram", "Tripp Prince", "Greta Murray", "Ashton Arellano", "Faye Cantrell", "Harris Chung",
    "Rivka Sierra", "Dayton Grimes", "Braelyn Barron", "Dustin Giles", "Bailee Martinez", "Alexander James",
    "Quinn Goodman", "Philip Odom", "Laylani Maddox", "Lyric Scott", "Aurora Lu", "Duncan Zamora",
    "Sierra Randall", "Trenton Church", "Ayleen Cantrell", "Harris Yoder", "Emerie Bradshaw", "Emory Cohen",
    "Destiny Lugo", "Santos Wiley", "Lauryn Trujillo", "Apollo Allen", "Riley Garner", "Sage Melendez",
    "Bethany Burgess", "Kolton Blevins", "Aila Waller", "Marley Stanley", "Gracelyn Reeves", "Clark Boone",
    "Mariam Rush", "Kaiser Khan", "Mabel Hess", "Lawrence Zavala", "Liv Roth", "Roy Hoover",
    "Virginia Olsen", "Skyler Gilbert", "Jocelyn Cortes", "Banks Hanson", "Mariana Molina", "Prince Benjamin",
    "Jianna Lopez", "Michael Maynard", "Carolyn Chan", "Frank Wallace", "Arianna Orozco", "Keanu Hester",
    "Zendaya Knapp", "Boden Hurst", "Adalee Cox", "Connor Pugh", "Landry Novak", "Bishop Rangel",
    "Gloria Day", "Kayson Cannon", "Noa Ford", "Luis Mayo", "Aarya Shannon", "Eliel Howard",
    "Sophie Shannon", "Eliel Bridges", "Elora Wilcox", "Jerry Mosley", "Zaniyah Daniels", "Xander Smith",
    "Olivia Gray", "Nicholas Daniels", "Ember Thomas", "Logan Jacobson", "Royal Patton", "Moises Friedman",
    "Aspyn Raymond", "Maurice Craig", "Brynn Marshall", "Kaiden Morgan", "Delilah Mayo", "Jericho Shields",
    "Analia Barajas", "Brennan Freeman", "Norah Moreno", "Myles Frost", "Paula Thomas", "Logan Knapp",
    "Linda Woods", "Zion Todd", "Zariah Andrade", "Abdiel Carrillo", "Kaylani Ramirez", "David Wall",
    "Jayda Rivers", "Bear Barnes", "Liliana Rosas", "Remi Walton", "Scarlet Lugo", "Santos Burns",
    "Emerson Hunter", "Archer Carr", "Rowan Gentry", "Magnus Salazar", "Freya Hodge", "Reign Gentry",
    "Amelie Peters", "Patrick Bryant", "Parker Wolfe", "Donovan Powers", "Michelle Kemp", "Melvin Browning",
    "Princess Rosales", "Wilder West", "Remi Zhang", "Isaias Cantu", "Galilea Combs", "Ahmad Garrison",
    "Cadence Russell", "Weston Wise", "Mira Curry", "Briggs Pearson", "Kiara Leonard", "Ricardo Ryan",
    "Morgan Powell", "Bennett Rush", "Maleah Barrera", "Makai Ahmed", "Jolie Powers", "Sean Whitaker",
    "Ivanna Guerra", "Leland Joseph", "Gracelynn Herring", "Henrik Grant", "Alaina Glass", "Allan Duffy",
    "Addisyn Swanson", "Hugo Mueller", "Imani Booker", "Dominik Buckley", "Theodora Lozano", "Boone Chung",
    "Rivka Carey", "Watson Floyd", "Yaretzi Henry", "Carlos Gutierrez", "Savannah Richard", "Ahmed Tyler",
    "Helena Travis", "Willie Collier", "Ivory Parsons", "Lewis Lang", "Amirah Hendrix", "Korbyn Moran",
    "Celeste Cain", "Benson Roman", "Astrid Newton", "Santino Dodson", "Etta Lin", "Conor Krueger",
    "Kamari McPherson", "Foster Turner", "Brooklyn Aguirre", "Andy Snyder", "Callie Khan", "Kendrick Walsh",
    "Leia Smith", "Liam Harris", "Penelope Henderson", "Beau Beltran", "Kaydence Winters", "Deandre Valencia",
    "Maddison Sandoval", "Brantley Frank", "Dior Wang", "Cohen Adams", "Stella Knapp", "Boden Jensen",
    "Jane Kline", "Ramon Hendricks", "Dani Nelson", "Dylan Welch", "Amira Jaramillo", "Riggs Navarro",
    "Winter Clayton", "Boston Farley", "Wrenley Bradley", "Richard Johnston", "Laila Chapman", "Knox Liu",
    "Kate Glover", "Mack Juarez", "Juliet Branch", "Keenan McDowell", "Rayna Corona", "Darian Jenkins",
    "Rylee Malone", "Ruben Nunez", "Mya Murillo", "Lance Delacruz", "Celine Morales", "Aaron Brandt",
    "Loretta Knight", "Beckett Lester", "Averi Hess", "Lawrence Dudley", "Hadleigh Felix", "Rodney Snyder",
    "Callie Sellers", "Madden Simon", "Kalani Huerta", "Douglas Solomon", "Mylah O’Connor", "Princeton Bartlett",
    "Aubrielle Kramer", "Kylan Leal", "Murphy Marin", "Aldo Mendoza", "Cora Beasley", "Stanley Black",
    "Molly Barnett", "Stephen O’brien", "Joanna Conway", "Orlando Bradley", "Vanessa Mueller", "Albert Orr",
    "Alaiya Weber", "Crew Leblanc", "Novalee Salas", "Zaiden Black", "Molly Everett", "Camilo Velasquez",
    "Esme Montgomery", "Maximiliano Gould", "Violeta Mills", "Alex Magana", "Amaris Vazquez", "Jesse Long",
    "Jade Olson", "Malachi Sharp", "Camryn Grimes", "Harlan Enriquez", "Nellie Keith", "Jagger Cannon",
    "Noa Magana", "Rey Clarke", "Kaitlyn Carroll", "Oscar Owen", "Mikayla Tate", "Dalton Chen",
    "Valeria Huang", "Ayaan Harding", "Aniya Gibbs", "Deacon Meyers", "Leyla Coffey", "Kody Richardson",
    "Allison Mayo", "Jericho Hahn", "Fallon Villarreal", "Nikolai Barber", "Cassidy Johnston", "Felix Padilla",
    "Maggie Bailey", "Axel Meyer", "Sara Armstrong", "Grant Morse", "Kairi Parker", "Caleb Parrish",
    "Tiana Abbott", "Kohen Fuentes", "Madeleine Gill", "Matthias Cantu", "Galilea Randall", "Trenton Morton",
    "Mallory Melton", "Lennon Singleton", "Malaysia Howe", "Alaric McBride", "Kelsey Francis", "Harvey Jensen",
    "Jane David", "Alonso Marquez", "Milani Hicks", "Maddox Gilmore", "Chanel Farrell", "Ty Davila",
    "Rayne Vega", "Aidan Perez", "Eleanor Graves", "Cesar Ingram", "Katie Savage", "Keaton Moyer",
    "Zola Oliver", "Karson Odom", "Laylani Lang", "Wells Conrad", "Bexley Howard", "Jeremiah Nixon",
    "Deborah Huffman", "Chris Ayers", "Simone Webb", "Lorenzo Marin", "Celia Dunlap", "Aries Reyes",
    "Audrey Morrow", "Kyree Sampson", "Meilani Flores", "Lincoln Coffey", "Paola Salgado", "Trace Lindsey",
    "Colette Black", "Matteo Mora", "Jemma Moyer", "Ahmir Clements", "Cara Copeland", "Axton Randall",
    "Christina Ballard", "Kenzo Patrick", "Lyra Montes", "Darren Stevenson", "Regina Fleming", "Fernando Ayers",
    "Simone Hahn", "Kabir Donaldson", "Natasha Jarvis", "Marlon Castro", "Eloise Henry", "Carlos Hess",
    "Kaliyah Gentry", "Magnus Burnett", "Emberly Stokes", "Santana Murray", "Faith King", "Julian Hobbs",
    "Lacey Coffey", "Kody Herrera", "Ximena Myers", "Adam Dudley", "Hadleigh Glenn", "Zaid Huang",
    "Francesca Baldwin", "Jaiden Huff", "Karsyn Anderson", "Jacob Kemp", "Anika Keller", "Nico Townsend",
    "Azalea Stuart", "Dion McLean", "Sky Daniel", "Grady Schmitt", "Queen Estrada", "Phoenix Andersen",
    "Zoie Sheppard", "Trent Morse", "Kairi Boyle", "Robin Velez", "Megan Perry", "Waylon Morrow",
    "Reyna Ray", "Arlo Giles", "Bailee Calderon", "Oakley Kerr", "Baylee Salazar", "Brody Schroeder",
    "Cameron Sierra", "Dayton Xiong", "Amayah Moses", "Niklaus Weaver", "Teagan Hill", "Isaac Buck",
    "Livia Palacios", "Thaddeus Chapman", "Zuri Rangel", "Saint Sierra", "Marceline Daniel", "Grady Freeman",
    "Norah Chan", "Frank Wallace", "Arianna Vance", "Casen Gregory", "Alaya Keller", "Nico Solomon",
    "Mylah Waters", "Maximilian Ortega", "Lilah Chung", "Ira Jaramillo", "Guadalupe Norton", "Callen Hurst",
    "Adalee Chan", "Frank Nichols", "Aliyah Dorsey", "Enoch Ramos", "Alice Schneider", "Raymond Ray",
    "Ruth Lamb", "Kaysen Lim", "Giavanna Lawrence", "Kaleb Hancock", "Katelyn Gibson", "Tyler Beasley",
    "Jaylah Peralta", "Dangelo Leonard", "Demi Gallegos", "Jonas Briggs", "Alia Morgan", "Hunter Roman",
    "Astrid Flores", "Lincoln Rangel", "Gloria Bowen", "Trevor McGuire", "April York", "Leandro Henson",
    "Kinslee Lewis", "Wyatt Benjamin", "Jianna Paul", "Noel Salazar", "Freya Gonzalez", "Ethan Sutton",
    "Izabella Flores", "Lincoln Gomez", "Natalie Serrano", "Milan Trujillo", "Danielle Gibson", "Tyler Frost",
    "Paula Henson", "Bellamy Mason", "Sienna Cantrell", "Harris Hickman", "Scarlette Guevara", "Tommy Burton",
    "Miriam Floyd", "Pierce Hunter", "Khloe Poole", "Quincy Richards", "Trinity Matthews", "Preston Palmer",
    "Juniper Dejesus", "Rio Mullins", "Maliyah Collins", "Miles Skinner", "Mara Flowers", "Saul Holmes",
    "Bailey Schroeder", "Izaiah Terrell", "Paityn Leal", "Cedric McMahon", "Belen Roman", "Kian Mullen",
    "Shay Shaffer", "Dexter Ruiz", "Emery Wilcox", "Jerry Stewart", "Maya Marsh", "Bo Best",
    "Lexie Cervantes", "Kamari Brandt", "Loretta Banks", "Martin Hodges", "Eve Vaughan", "Castiel McCoy",
    "Mckenzie Miles", "Jared Beck", "Gia Roberson", "Shepherd O’Donnell", "Bellamy Franco", "Gage Manning",
    "Jennifer Ferguson", "Miguel Daugherty", "Magdalena Le", "Damien Lloyd", "Emely Buchanan", "Enrique Knight",
    "Gracie Day", "Kayson Hamilton", "Mackenzie Reyna", "Reginald Shepard", "Noor Casey", "Armando Knox",
    "Kallie Ellis", "Cole Ortega", "Lilah Davis", "Lucas Anthony", "Macy Correa", "Zakai Marquez",
    "Milani Vance", "Casen Woodward", "Drew Maddox", "Lyric Solis", "Miracle Sellers", "Madden Patrick",
    "Lyra Thornton", "Malik Flores", "Emilia Campbell", "Christopher Rivers", "Kiana Perry", "Waylon Sheppard",
    "Veda Anthony", "Shiloh Fletcher", "Anaya Smith", "Liam Pitts", "Nala Wolf", "Jase Palacios",
    "Bria Bush", "Tyson Tapia", "Michaela Campos", "Gideon Pennington"
]

# Extract names and separate into first and last names
first_names = [name.split()[0] for name in names]
last_names = [name.split()[1] for name in names]

# first_names[:10], last_names[:10] 

# Function to generate a random salary between a specified range
def generate_salary():
    return round(random.uniform(75000, 250000), 2)


# Create hiring manager dataset
data = {
    "First Name": [random.choice(first_names) for _ in range(1500)],
    "Last Name": [random.choice(last_names) for _ in range(1500)],
    "Job Title": [random.choice(job_titles) for _ in range(1500)],
    "Salary": [generate_salary() for _ in range(1500)],
    "Random Number": [random.randint(1, 100) for _ in range(1500)]
}

# Convert to DataFrame
hiringManagerdf = pd.DataFrame(data)

# Save to CSV
hiringManagerdf.to_csv("hiringManagersData.csv", index=False)

# Display the DataFrame
hiringManagerdf.head()


# Sample lists of African American first and last names
african_american_first_names = [
    "Andre", "Darius", "Jamal", "Keshawn", "Malik", "Terrence", "Xavier", "Aaliyah", "Ebony", "Imani", 
    "Jasmine", "Keisha", "Latoya", "Nia", "Shanice", "Tanisha", "Zuri", "Brianna", "Serenity", "Jayla", 
    "Brielle", "Jocelyn", "Ava", "Aria", "Riley", "Zoe", "Layla", "Skylar", "Camila", "Mila", "Genesis", 
    "Kennedy", "Victoria", "Aiden", "Elijah", "Isaiah", "Josiah", "Jayden", "Michael", "Malik", "Xavier", 
    "Amir", "Jaxon", "Jaden", "Ethan", "Noah", "Cameron", "Carter", "Mason", "Caleb", "Jeremiah"
]

african_american_last_names = [
    "Johnson", "Williams", "Brown", "Jones", "Davis", "Smith", "Thomas", "Jackson", "Harris", "Martin",
    "Thompson", "White", "Lee", "Walker", "Robinson", "Lewis", "Young", "Hall", "Allen", "King", 
    "Wright", "Scott", "Green", "Adams", "Baker", "Nelson", "Hill", "Campbell", "Mitchell", "Carter", 
    "Roberts", "Phillips", "Evans", "Turner", "Torres", "Parker", "Collins", "Edwards", "Stewart", "Flores", 
    "Morris", "Nguyen", "Murphy", "Rivera", "Cook", "Rogers", "Morgan", "Peterson", "Cooper", "Reed"
]

# Sample lists of European/Russian first and last names
european_first_names = [
    "Aleksandr", "Boris", "Dmitry", "Igor", "Ivan", "Maxim", "Nikolai", "Sergei", "Viktor", "Yuri", "Anna", 
    "Daria", "Elena", "Irina", "Katarina", "Maria", "Natasha", "Olga", "Svetlana", "Tatiana", "Alexei", 
    "Andrei", "Mikhail", "Pavel", "Roman", "Semyon", "Vadim", "Vasiliy", "Anton", "Arkady", "Bogdan", 
    "Denis", "Efim", "Fyodor", "Gennady", "Grigory", "Ilya", "Konstantin", "Anastasia", "Galina", "Inna", 
    "Ludmila", "Oksana", "Polina", "Sonia", "Valentina", "Zinaida", "Zoya"
]

european_last_names = [
    "Ivanov", "Petrov", "Sidorov", "Kuznetsov", "Popov", "Vasilyev", "Smirnov", "Volkov", "Fedorov", "Mikhailov",
    "Novikov", "Morozov", "Stepanov", "Orlov", "Alekseev", "Nikolaev", "Pavlov", "Semenov", "Golubev", "Vinogradov",
    "Bogdanov", "Vorobyov", "Zaitsev", "Sorokin", "Yakovlev", "Makarov", "Matveev", "Afanasev", "Rogov", "Kozlov",
    "Gusev", "Alyoshin", "Krylov", "Belyaev", "Tikhomirov", "Nikitin", "Polyakov", "Tarasov", "Efimov", "Davydov",
    "Savelyev", "Samsonov", "Babanin", "Druzhinin", "Vasiliev", "Zotov", "Larionov", "Mitrofanov", "Barkov", "Chernov"
]

# Function to generate random names
def generate_random_names(first_names_list, last_names_list, count):
    first_names = random.choices(first_names_list, k=count)
    last_names = random.choices(last_names_list, k=count)
    return first_names, last_names

# Set the seed for reproducibility
random.seed(42)

# Generate 750 African American and 750 European names
african_american_first, african_american_last = generate_random_names(african_american_first_names, african_american_last_names, 750)
european_first, european_last = generate_random_names(european_first_names, european_last_names, 750)

# Combine the samples and create a DataFrame
combined_first_names = african_american_first + european_first
combined_last_names = african_american_last + european_last
labels = ["African"] * 750 + ["Non-African"] * 750

data = {
    "First Name": combined_first_names,
    "Last Name": combined_last_names,
    "Category": labels
}

resumeTargetListdf = pd.DataFrame(data)

# Save to CSV
resumeTargetListdf.to_csv("resumeTargetListdf.csv", index=False)

#print(resumeTargetListdf.head())


combined_df = pd.concat([hiringManagerdf, resumeTargetListdf], axis=1)


# Here is where we assign a 1 if applicant has been hired and a 0 if its not been hired. 
# We will assign a 1 on a random number basis if the number is less than 50 and 0 otherwise. 
# Furthermore, Id like to create 3 different testable samples to show statistical diffenrences,
# based on the where the data is sliced for test purposes. 

def categorize_is_hired(row):
    return 1 if row['Random Number'] < 30 else 0

# Create a new dataframe with the is_hired field
sampleOneCombined_df = combined_df
sampleTwoCombined_df = combined_df.copy()
sampleThreeCombined_df = combined_df.copy()

sampleOneCombined_df['is_hired'] = sampleOneCombined_df.apply(categorize_is_hired, axis=1)

# Save to CSV
sampleOneCombined_df.to_csv("sampleOneCombinedIsHiredData.csv", index=False)


def categorize_is_hired(row):
    return 1 if row['Random Number'] < 60 else 0

sampleTwoCombined_df['is_hired'] = sampleTwoCombined_df.apply(categorize_is_hired, axis=1)

sampleTwoCombined_df.to_csv("sampleTwoCombinedIsHiredData.csv", index=False)


def categorize_is_hired(row):
    return 1 if row['Random Number'] < 90 else 0

sampleThreeCombined_df['is_hired'] = sampleThreeCombined_df.apply(categorize_is_hired, axis=1)

sampleThreeCombined_df.to_csv("sampleThreeCombinedIsHiredData.csv", index=False)