from app import db
from sqlalchemy import text

insert_customer = text(
    """INSERT INTO customer VALUES
    ('user1', 'password', 'foo', 'bar', '12345678', '8 Somapah Rd', '12345678'),
    ('user2', 'password2', 'foo', 'bar', '12345678', '8 Somapah Rd', '12345678')"""
)

delete_customer = text(
    'DELETE FROM customer'
)

insert_store_manager = text(
    """INSERT INTO store_manager VALUES
    ('store_manager1', 'password')"""
)

delete_store_manager = text(
    'DELETE FROM store_manager'
)

insert_books = text(
    """INSERT INTO book ("ISBN", title, authors, publisher, year_of_publication, stock, price, format, subject, keywords) VALUES
    ('9780321197849', 'An Introduction to Database Systems', '{"C.J. Date"}', 'Pearson', 2003, 5, 206.42, 'hardcover', 'Database', '{"database", "computer science"}'),
    ('9781783555130', 'Python Machine Learning', '{Sebastian Raschka}', 'Packt Publishing', 2015, 10, 40.49, 'softcover', 'Machine Learning', '{"machine learning", "data science", "computer science", "statistical learning"}'),
    ('9781461471370', 'An Introduction to Statistical Learning: with Applications in R', '{"Gareth James", "Daniela Witten", "Trevor Hastie", "Robert Tibshirani"}', 'Springer', 2013, 2, 72.62, 'hardcover', 'Statistical Learning', '{"machine learning", "data science", "computer science", "statistical learning"}'),
    ('9781449389673','Photoshop Elements 9: The Missing Manual','{"Barbara Brundage"}','Pogue Press',2010,59, 57.61, 'softcover', 'Foo', '{"Photoshop", "Elements", "9:", "The", "Missing", "Manual"}'),
    ('9781594487712','Where Good Ideas Come From: The Natural History of Innovation','{"Steven Johnson"}','Riverhead Hardcover',2010,36, 22.8, 'hardcover', 'Foo', '{"Where", "Good", "Ideas", "Come", "From:", "The", "Natural", "History", "of", "Innovation"}'),
    ('9780321474049','The Digital Photography Book','{"Scott Kelby"}','Peachpit Press',2006,53, 94.1, 'softcover', 'Foo', '{"The", "Digital", "Photography", "Book"}'),
    ('9780684801520','The Great Gatsby','{"F. Scott Fitzgerald"}','Scribner',1995,99, 43.45, 'hardcover', 'Foo', '{"The", "Great", "Gatsby"}'),
    ('9780803612259','Davis s Drug Guide For Nurses (book With Cd-rom) And Mednotes: Nurse s Pocket Pharmacology Guide','{"Judith Hopfer Deglin", " April Hazard Vallerand"}','F. A. Davis Company',2004,66, 41.51, 'hardcover', 'Foo', '{"Davis", "s", "Drug", "Guide", "For", "Nurses", "(book", "With", "Cd-rom)", "And", "Mednotes:", "Nurse", "s", "Pocket", "Pharmacology", "Guide"}'),
    ('9781111529024','Microsoft Office 2007: Introductory Concepts and Techniques, Premium Video Edition (Book Only)','{"Gary B. Shelly", " Thomas J. Cashman", " Misty E. Vermaat"}','Course Technology',2010,53, 19.79, 'softcover', 'Foo', '{"Microsoft", "Office", "2007:", "Introductory", "Concepts", "and", "Techniques,", "Premium", "Video", "Edition", "(Book", "Only)"}'),
    ('9780262513593','The Future of Learning Institutions in a Digital Age (John D. and Catherine T. MacArthur Foundation Reports on Digital Media and Learning)','{"Cathy N. Davidson", " David Theo Goldberg"}','The MIT Press ',2009,79, 1.78, 'softcover', 'Foo', '{"The", "Future", "of", "Learning", "Institutions", "in", "a", "Digital", "Age", "(John", "D.", "and", "Catherine", "T.", "MacArthur", "Foundation", "Reports", "on", "Digital", "Media", "and", "Learning)"}'),
    ('9780470547816','The New Rules of Marketing and PR: How to Use Social Media, Blogs, News Releases, Online Video, and Viral Marketing to Reach Buyers Directly, 2nd Edition','{"David Meerman Scott"}','Wiley',2010,62, 25.89, 'softcover', 'Foo', '{"The", "New", "Rules", "of", "Marketing", "and", "PR:", "How", "to", "Use", "Social", "Media,", "Blogs,", "News", "Releases,", "Online", "Video,", "and", "Viral", "Marketing", "to", "Reach", "Buyers", "Directly,", "2nd", "Edition"}'),
    ('9780321344755','Dont Make Me Think: A Common Sense Approach to Web Usability, 2nd Edition','{"Steve Krug"}','New Riders Press',2005,81, 48.02, 'softcover', 'Foo', '{"Dont", "Make", "Me", "Think:", "A", "Common", "Sense", "Approach", "to", "Web", "Usability,", "2nd", "Edition"}'),
    ('9780393072228','The Shallows: What the Internet Is Doing to Our Brains','{"Nicholas Carr"}','W. W. Norton & Company ',2010,20, 44.61, 'hardcover', 'Foo', '{"The", "Shallows:", "What", "the", "Internet", "Is", "Doing", "to", "Our", "Brains"}'),
    ('9780071701334','CompTIA A+ Certification All-in-One Exam Guide, Seventh Edition (Exams 220-701 & 220-702)','{"Michael Meyers"}','McGraw-Hill Osborne Media',2010,47, 14.86, 'hardcover', 'Foo', '{"CompTIA", "A+", "Certification", "All-in-One", "Exam", "Guide,", "Seventh", "Edition", "(Exams", "220-701", "&", "220-702)"}'),
    ('9780470523988','Windows 7 For Dummies Book + DVD Bundle','{"Andy Rathbone"}','For Dummies',2009,7, 60.56, 'softcover', 'Foo', '{"Windows", "7", "For", "Dummies", "Book", "+", "DVD", "Bundle"}'),
    ('9780262033848','Introduction to Algorithms, Third Edition','{"Thomas H. Cormen", " Charles E. Leiserson", " Ronald L. Rivest", " Clifford Stein"}','The MIT Press',2009,84, 43.19, 'hardcover', 'Foo', '{"Introduction", "to", "Algorithms,", "Third", "Edition"}'),
    ('9780321295354','Algorithm Design','{"Jon Kleinberg", " Eva Tardos"}','Addison Wesley',2005,29, 46.31, 'hardcover', 'Foo', '{"Algorithm", "Design"}'),
    ('9780321441461','Data Structures and Algorithm Analysis in C++ (3rd Edition)','{"Mark A. Weiss"}','Addison Wesley',2006,26, 55.35, 'hardcover', 'Foo', '{"Data", "Structures", "and", "Algorithm", "Analysis", "in", "C++", "(3rd", "Edition)"}'),
    ('9781848000698','The Algorithm Design Manual','{"Steven S. Skiena"}','Springer',2008,31, 55.74, 'hardcover', 'Foo', '{"The", "Algorithm", "Design", "Manual"}'),
    ('9780072467505','Introduction to Computing Systems: From bits & gates to C & beyond','{"Yale Patt", " Sanjay Patel"}','McGraw-Hill Science/Engineering/Math',2003,26, 58.76, 'hardcover', 'Foo', '{"Introduction", "to", "Computing", "Systems:", "From", "bits", "&", "gates", "to", "C", "&", "beyond"}'),
    ('9781449389550','Hackers & Painters: Big Ideas from the Computer Age','{"Paul Graham"}','O Reilly Media',2010,1, 55.12, 'softcover', 'Foo', '{"Hackers", "&", "Painters:", "Big", "Ideas", "from", "the", "Computer", "Age"}'),
    ('9780470383261','Data Structures and Algorithms in Java','{"Michael T. Goodrich", " Roberto Tamassia"}','Wiley',2010,35, 9.99, 'hardcover', 'Foo', '{"Data", "Structures", "and", "Algorithms", "in", "Java"}'),
    ('9780596529321','Programming Collective Intelligence: Building Smart Web 2.0 Applications','{"Toby Segaran"}','O Reilly Media',2007,47, 77.75, 'softcover', 'Foo', '{"Programming", "Collective", "Intelligence:", "Building", "Smart", "Web", "2.0", "Applications"}'),
    ('9781933988665','Algorithms of the Intelligent Web','{"Haralambos Marmanis", " Dmitry Babenko"}','Manning Publications',2009,64, 32.38, 'softcover', 'Foo', '{"Algorithms", "of", "the", "Intelligent", "Web"}'),
    ('9780321370136','Data Structures and Algorithm Analysis in Java (2nd Edition)','{"Mark A. Weiss"}','Addison Wesley',2006,27, 66.3, 'hardcover', 'Foo', '{"Data", "Structures", "and", "Algorithm", "Analysis", "in", "Java", "(2nd", "Edition)"}'),
    ('9780321358288','Introduction to the Design and Analysis of Algorithms (2nd Edition)','{"Anany V. Levitin"}','Addison Wesley',2006,2, 84.38, 'softcover', 'Foo', '{"Introduction", "to", "the", "Design", "and", "Analysis", "of", "Algorithms", "(2nd", "Edition)"}'),
    ('9780596516246','Algorithms in a Nutshell (In a Nutshell (O Reilly))','{"George T. Heineman", " Gary Pollice", " Stanley Selkow"}','O Reilly Media',2008,59, 6.33, 'softcover', 'Foo', '{"Algorithms", "in", "a", "Nutshell", "(In", "a", "Nutshell", "(O", "Reilly))"}'),
    ('9780596802356','Data Analysis with Open Source Tools','{"Philipp K. Janert"}','O Reilly Media',2010,55, 70.9, 'softcover', 'Foo', '{"Data", "Analysis", "with", "Open", "Source", "Tools"}'),
    ('9780672329166','PHP and MySQL Web Development (4th Edition)','{"Luke Welling", " Laura Thomson"}','Addison-Wesley Professional',2008,28, 15.56, 'softcover', 'Foo', '{"PHP", "and", "MySQL", "Web", "Development", "(4th", "Edition)"}'),
    ('9780672325670','Sams Teach Yourself SQL in 10 Minutes (3rd Edition)','{"Ben Forta"}','Sams',2004,43, 91.11, 'softcover', 'Foo', '{"Sams", "Teach", "Yourself", "SQL", "in", "10", "Minutes", "(3rd", "Edition)"}'),
    ('9780538469685','Database Systems: Design, Implementation, and Management (with Bind-In Printed Access Card)','{"Carlos Coronel", " Steven Morris", " Peter Rob"}','Course Technology',2009,71, 19.28, 'hardcover', 'Foo', '{"Database", "Systems:", "Design,", "Implementation,", "and", "Management", "(with", "Bind-In", "Printed", "Access", "Card)"}'),
    ('9781423905899','New Perspectives on Microsoft Office Access 2007, Comprehensive','{"Joseph J. Adamski", " Kathy T. Finnegan"}','Course Technology',2007,62, 93.38, 'softcover', 'Foo', '{"New", "Perspectives", "on", "Microsoft", "Office", "Access", "2007,", "Comprehensive"}'),
    ('9780136086208','Fundamentals of Database Systems (6th Edition) (Alternative eText Formats)','{"Ramez Elmasri", " Shamkant Navathe"}','Addison Wesley',2010,45, 60.41, 'hardcover', 'Foo', '{"Fundamentals", "of", "Database", "Systems", "(6th", "Edition)", "(Alternative", "eText", "Formats)"}'),
    ('9781423905875','New Perspectives on Microsoft Office Access 2007, Brief (New Perspectives Series)','{"Joseph J. Adamski", " Kathy T. Finnegan"}','Course Technology',2007,24, 97.7, 'softcover', 'Foo', '{"New", "Perspectives", "on", "Microsoft", "Office", "Access", "2007,", "Brief", "(New", "Perspectives", "Series)"}'),
    ('9781423901471','Concepts of Database Management (Sam 2007 Compatible Products)','{"Philip J. Pratt", " Joseph J. Adamski"}','Course Technology',2007,48, 9.98, 'softcover', 'Foo', '{"Concepts", "of", "Database", "Management", "(Sam", "2007", "Compatible", "Products)"}'),
    ('9781418843410','Microsoft Office Access 2007: Comprehensive Concepts and Techniques (Shelly Cashman)','{"Gary B. Shelly", " Thomas J. Cashman", " Philip J. Pratt", " Mary Z. Last"}','Course Technology',2007,47, 52.8, 'softcover', 'Foo', '{"Microsoft", "Office", "Access", "2007:", "Comprehensive", "Concepts", "and", "Techniques", "(Shelly", "Cashman)"}'),
    ('9780072465631','Database Management Systems','{"Raghu Ramakrishnan", " Johannes Gehrke"}','McGraw-Hill Science/Engineering/Math',2002,57, 23.58, 'hardcover', 'Foo', '{"Database", "Management", "Systems"}'),
    ('9781449389734','Hadoop: The Definitive Guide','{"Tom White"}','Yahoo Press',2010,55, 90.52, 'softcover', 'Foo', '{"Hadoop:", "The", "Definitive", "Guide"}'),
    ('9781423925811','Fundamentals of Information Systems','{"Ralph Stair", " George Reynolds"}','Course Technology',2008,41, 23.35, 'softcover', 'Foo', '{"Fundamentals", "of", "Information", "Systems"}'),
    ('9780123744937','Computer Organization and Design, Fourth Edition: The Hardware/Software Interface (The Morgan Kaufmann Series in Computer Architecture and Design)','{"David A. Patterson", " John L. Hennessy"}','Morgan Kaufmann',2008,15, 22.89, 'softcover', 'Foo', '{"Computer", "Organization", "and", "Design,", "Fourth", "Edition:", "The", "Hardware/Software", "Interface", "(The", "Morgan", "Kaufmann", "Series", "in", "Computer", "Architecture", "and", "Design)"}'),
    ('9780136079675','Computer Networking: A Top-Down Approach (5th Edition)','{"James F. Kurose", " Keith W. Ross"}','Addison Wesley',2009,43, 54.02, 'hardcover', 'Foo', '{"Computer", "Networking:", "A", "Top-Down", "Approach", "(5th", "Edition)"}'),
    ('9780071602174','CISSP All-in-One Exam Guide, Fifth Edition','{"Shon Harris"}','McGraw-Hill Osborne Media',2010,51, 78.32, 'hardcover', 'Foo', '{"CISSP", "All-in-One", "Exam", "Guide,", "Fifth", "Edition"}'),
    ('9781423902454','Network+ Guide to Networks (Networking (Course Technology))','{"Tamara Dean"}','Course Technology',2009,34, 5.09, 'softcover', 'Foo', '{"Network+", "Guide", "to", "Networks", "(Networking", "(Course", "Technology))"}'),
    ('9781587201837','CCNA Official Exam Certification Library (Exam 640-802), Third Edition (Containing ICND1 and ICND2 Second Edition Exam Certification Guides)','{"Wendell Odom"}','Cisco Press',2007,13, 54.89, 'hardcover', 'Foo', '{"CCNA", "Official", "Exam", "Certification", "Library", "(Exam", "640-802),", "Third", "Edition", "(Containing", "ICND1", "and", "ICND2", "Second", "Edition", "Exam", "Certification", "Guides)"}'),
    ('9781428340664','Security+ Guide to Network Security Fundamentals','{"Mark Ciampa"}','Course Technology',2008,71, 86.61, 'softcover', 'Foo', '{"Security+", "Guide", "to", "Network", "Security", "Fundamentals"}'),
    ('9781587132087','Network Fundamentals, CCNA Exploration Companion Guide','{"Mark Dye", " Rick McDonald", " Antoon Rufi"}','Cisco Press ',2007,93, 76.81, 'hardcover', 'Foo', '{"Network", "Fundamentals,", "CCNA", "Exploration", "Companion", "Guide"}'),
    ('9781435498839','Guide to Computer Forensics and Investigations','{"Bill Nelson", " Amelia Phillips", " Christopher Steuart"}','Course Technology',2009,31, 88.99, 'softcover', 'Foo', '{"Guide", "to", "Computer", "Forensics", "and", "Investigations"}'),
    ('9781423901778','Principles of Information Security','{"Michael E. Whitman", " Herbert J. Mattord"}','Course Technology',2007,12, 92.55, 'softcover', 'Foo', '{"Principles", "of", "Information", "Security"}'),
    ('9780596807733','Building Wireless Sensor Networks: with ZigBee, XBee, Arduino, and Processing','{"Robert Faludi"}','O Reilly Media',2010,52, 41.28, 'softcover', 'Foo', '{"Building", "Wireless", "Sensor", "Networks:", "with", "ZigBee,", "XBee,", "Arduino,", "and", "Processing"}'),
    ('9780470110089','CCNA: Cisco Certified Network Associate Study Guide: Exam 640-802','{"Todd Lammle"}','Sybex',2007,88, 94.9, 'softcover', 'Foo', '{"CCNA:", "Cisco", "Certified", "Network", "Associate", "Study", "Guide:", "Exam", "640-802"}'),
    ('9780735627086','MCTS Self-Paced Training Kit (Exam 70-680): Configuring Windows 7','{"Ian McLean", " Orin Thomas"}','Microsoft Press',2009,26, 29.91, 'hardcover', 'Foo', '{"MCTS", "Self-Paced", "Training", "Kit", "(Exam", "70-680):", "Configuring", "Windows", "7"}'),
    ('9780470128725','Operating System Concepts','{"Abraham Silberschatz", " Peter B. Galvin", " Greg Gagne"}','Wiley',2008,18, 28.66, 'hardcover', 'Foo', '{"Operating", "System", "Concepts"}'),
    ('9780735626652','Windows 7 Inside Out','{"Ed Bott", " Carl Siechert", " Craig Stinson"}','Microsoft Press',2009,11, 45.11, 'softcover', 'Foo', '{"Windows", "7", "Inside", "Out"}'),
    ('9780131480056','UNIX and Linux System Administration Handbook (4th Edition)','{"Evi Nemeth", " Garth Snyder", " Trent R. Hein", " Ben Whaley"}','Prentice Hall',2010,76, 52.94, 'softcover', 'Foo', '{"UNIX", "and", "Linux", "System", "Administration", "Handbook", "(4th", "Edition)"}'),
    ('9780205020409','Using SPSS for Windows and Macintosh: Analyzing and Understanding Data (6th Edition)','{"Samuel B. Green", " Neil J. Salkind"}','Prentice Hall',2010,43, 60.36, 'softcover', 'Foo', '{"Using", "SPSS", "for", "Windows", "and", "Macintosh:", "Analyzing", "and", "Understanding", "Data", "(6th", "Edition)"}'),
    ('9780735626669','Windows 7 Plain & Simple','{"Jerry Joyce", " Marianne Moon"}','Microsoft Press',2009,36, 21.7, 'softcover', 'Foo', '{"Windows", "7", "Plain", "&", "Simple"}'),
    ('9780470533338','Professional SharePoint 2010 Administration','{"Todd Klindt", " Shane Young", " Steve Caravajal"}','Wrox ',2010,4, 66.28, 'softcover', 'Foo', '{"Professional", "SharePoint", "2010", "Administration"}'),
    ('9780131367364','Practical Guide to Linux Commands, Editors, and Shell Programming, A (2nd Edition)','{"Mark G. Sobell"}','Prentice Hall',2009,46, 68.39, 'softcover', 'Foo', '{"Practical", "Guide", "to", "Linux", "Commands,", "Editors,", "and", "Shell", "Programming,", "A", "(2nd", "Edition)"}'),
    ('9781430227007','iPhone and iPad Apps for Absolute Beginners (Getting Started)','{"Rory Lewis"}','Apress',2010,10, 76.81, 'softcover', 'Foo', '{"iPhone", "and", "iPad", "Apps", "for", "Absolute", "Beginners", "(Getting", "Started)"}'),
    ('9780596517748','JavaScript: The Good Parts','{"Douglas Crockford"}','Yahoo Press',2008,79, 10.99, 'softcover', 'Foo', '{"JavaScript:", "The", "Good", "Parts"}'),
    ('9780596513986','Learning Python, 3rd Edition','{"Mark Lutz"}','O Reilly Media',2007,5, 33.72, 'softcover', 'Foo', '{"Learning", "Python,", "3rd", "Edition"}'),
    ('9780735619678','Code Complete: A Practical Handbook of Software Construction','{"Steve McConnell"}','Microsoft Press',2004,85, 33.83, 'softcover', 'Foo', '{"Code", "Complete:", "A", "Practical", "Handbook", "of", "Software", "Construction"}'),
    ('9780201835953','The Mythical Man-Month: Essays on Software Engineering, Anniversary Edition (2nd Edition)','{"Frederick P. Brooks"}','Addison-Wesley Professional',1995,62, 90.31, 'softcover', 'Foo', '{"The", "Mythical", "Man-Month:", "Essays", "on", "Software", "Engineering,", "Anniversary", "Edition", "(2nd", "Edition)"}'),
    ('9780596007126','Head First Design Patterns','{"Elisabeth Freeman", " Eric Freeman", " Bert Bates", " Kathy Sierra"}','O Reilly Media',2004,90, 21.27, 'softcover', 'Foo', '{"Head", "First", "Design", "Patterns"}'),
    ('9780596101992','JavaScript: The Definitive Guide','{"David Flanagan"}','O Reilly Media',2006,24, 47.85, 'softcover', 'Foo', '{"JavaScript:", "The", "Definitive", "Guide"}'),
    ('9780470565520','Professional Android 2 Application Development (Wrox Programmer to Programmer)','{"Reto Meier"}','Wrox',2010,26, 23.96, 'softcover', 'Foo', '{"Professional", "Android", "2", "Application", "Development", "(Wrox", "Programmer", "to", "Programmer)"}'),
    ('9780321579362','Succeeding with Agile: Software Development Using Scrum','{"Mike Cohn"}','Addison-Wesley Professional',2009,26, 74.86, 'softcover', 'Foo', '{"Succeeding", "with", "Agile:", "Software", "Development", "Using", "Scrum"}'),
    ('9780716744641','Quantitative Chemical Analysis','{"Daniel C. Harris"}','W. H. Freeman',2002,76, 89.14, 'hardcover', 'Foo', '{"Quantitative", "Chemical", "Analysis"}'),
    ('9780470115398','Transport Phenomena, Revised 2nd Edition','{"R. Byron Bird", " Warren E. Stewart", " Edwin N. Lightfoot"}','John Wiley & Sons, Inc.',2006,19, 45.64, 'hardcover', 'Foo', '{"Transport", "Phenomena,", "Revised", "2nd", "Edition"}'),
    ('9780073104454','Introduction to Chemical Engineering Thermodynamics (The Mcgraw-Hill Chemical Engineering Series)','{"J.M. Smith", " Hendrick Van Ness", " Michael Abbott"}','McGraw-Hill Science/Engineering/Math',2004,76, 87.06, 'hardcover', 'Foo', '{"Introduction", "to", "Chemical", "Engineering", "Thermodynamics", "(The", "Mcgraw-Hill", "Chemical", "Engineering", "Series)"}'),
    ('9780470128688','Fundamentals of Momentum, Heat and Mass Transfer','{"James Welty", " Charles E. Wicks", " Gregory L. Rorrer", " Robert E. Wilson"}','Wiley',2007,40, 13.32, 'hardcover', 'Foo', '{"Fundamentals", "of", "Momentum,", "Heat", "and", "Mass", "Transfer"}'),
    ('9780130473943','Elements of Chemical Reaction Engineering (4th Edition)','{"H. Scott Fogler"}','Prentice Hall',2005,68, 78.97, 'hardcover', 'Foo', '{"Elements", "of", "Chemical", "Reaction", "Engineering", "(4th", "Edition)"}'),
    ('9780073044811','Basic Biomechanics','{"Susan Hall"}','McGraw-Hill Humanities/Social Sciences/Languages',2006,46, 51.78, 'softcover', 'Foo', '{"Basic", "Biomechanics"}'),
    ('9780470128671','Process Dynamics and Control','{"Dale E. Seborg", " Duncan A. Mellichamp", " Thomas F. Edgar", " Francis J. Doyle III"}','Wiley',2010,67, 20.58, 'hardcover', 'Foo', '{"Process", "Dynamics", "and", "Control"}'),
    ('9780077295462','Fluid Mechanics with Student Resources DVD','{"Yunus Cengel", " John Cimbala"}','McGraw-Hill Science/Engineering/Math',2009,47, 17.33, 'hardcover', 'Foo', '{"Fluid", "Mechanics", "with", "Student", "Resources", "DVD"}'),
    ('9780072424119','Introduction to Environmental Engineering','{"Mackenzie Davis", " David Cornwell"}','McGraw-Hill Science/Engineering/Math',2006,6, 23.97, 'hardcover', 'Foo', '{"Introduction", "to", "Environmental", "Engineering"}'),
    ('9780130847898','Separation Process Engineering (2nd Edition)','{"Phillip C. Wankat"}','Prentice Hall',2006,87, 78.49, 'hardcover', 'Foo', '{"Separation", "Process", "Engineering", "(2nd", "Edition)"}'),
    ('9780077221409','Mechanics of Materials','{"Ferdinand Beer", " Jr.", " E. Russell Johnston", " John DeWolf", " David Mazurek"}','McGraw-Hill Science/Engineering/Math',2008,18, 79.77, 'hardcover', 'Foo', '{"Mechanics", "of", "Materials"}'),
    ('9781591261292','Civil Engineering Reference Manual for the PE Exam','{"Michael R. Lindeburg PE"}','Professional Publications, Inc.',2008,33, 75.6, 'hardcover', 'Foo', '{"Civil", "Engineering", "Reference", "Manual", "for", "the", "PE", "Exam"}'),
    ('9780470279274','Design of Reinforced Concrete','{"Jack C. McCormac", " Russell Brown"}','Wiley',2008,67, 82.3, 'hardcover', 'Foo', '{"Design", "of", "Reinforced", "Concrete"}'),
    ('9780470290750','Principles of Highway Engineering and Traffic Analysis','{"Fred L. Mannering", " Scott S. Washburn", " Walter P. Kilareski"}','Wiley',2008,32, 2.33, 'hardcover', 'Foo', '{"Principles", "of", "Highway", "Engineering", "and", "Traffic", "Analysis"}'),
    ('9780132281416','Reinforced Concrete: Mechanics and Design (5th Edition)','{"James K. Wight", " James G. MacGregor"}','Prentice Hall',2008,86, 61.84, 'hardcover', 'Foo', '{"Reinforced", "Concrete:", "Mechanics", "and", "Design", "(5th", "Edition)"}'),
    ('9780486676203','Partial Differential Equations for Scientists and Engineers (Dover Books on Advanced Mathematics)','{"Stanley J. Farlow"}','Dover Publications ',1993,47, 76.73, 'softcover', 'Foo', '{"Partial", "Differential", "Equations", "for", "Scientists", "and", "Engineers", "(Dover", "Books", "on", "Advanced", "Mathematics)"}'),
    ('9780136110583','Materials for Civil and Construction Engineers (3rd Edition) (Alternative eText Formats)','{"Michael S. Mamlouk", " John P. Zaniewski"}','Prentice Hall',2010,83, 24.16, 'hardcover', 'Foo', '{"Materials", "for", "Civil", "and", "Construction", "Engineers", "(3rd", "Edition)", "(Alternative", "eText", "Formats)"}'),
    ('9780495411307','Principles of Geotechnical Engineering','{"Braja M. Das"}','CL-Engineering',2009,82, 67.58, 'hardcover', 'Foo', '{"Principles", "of", "Geotechnical", "Engineering"}'),
    ('9781425318758','Experiments With Alternate Currents Of High Potential And High Frequency','{"Nikola Tesla"}','Kessinger Publishing, LLC ',2005,5, 46.63, 'softcover', 'Foo', '{"Experiments", "With", "Alternate", "Currents", "Of", "High", "Potential", "And", "High", "Frequency"}'),
    ('9780877659143','National Electrical Code 2011 (National Fire Protection Association National Electrical Code)','{"National Fire Protection Association"}','Delmar Cengage Learning',2010,45, 20.73, 'softcover', 'Foo', '{"National", "Electrical", "Code", "2011", "(National", "Fire", "Protection", "Association", "National", "Electrical", "Code)"}'),
    ('9780131465923','Electric Circuits','{"James W. Nilsson", " Susan Riedel"}','Prentice Hall',2004,92, 29.69, 'hardcover', 'Foo', '{"Electric", "Circuits"}'),
    ('9780877657903','National Electrical Code 2008 (National Fire Protection Association National Electrical Code)','{"National Fire Protection Association"}','National Fire Protection Association',2007,6, 7.15, 'softcover', 'Foo', '{"National", "Electrical", "Code", "2008", "(National", "Fire", "Protection", "Association", "National", "Electrical", "Code)"}'),
    ('9780131470460','Electrical Engineering: Principles & Applications ','{"Allan R. Hambley"}','Prentice Hall',2004,80, 9.41, 'hardcover', 'Foo', '{"Electrical", "Engineering:", "Principles", "&", "Applications"}'),
    ('9780072493504','Fundamentals of Electric Circuits with CD-ROM','{"Charles K. Alexander", " Matthew Sadiku"}','McGraw-Hill Science/Engineering/Math',2003,38, 59.07, 'hardcover', 'Foo', '{"Fundamentals", "of", "Electric", "Circuits", "with", "CD-ROM"}'),
    ('9780195142518','Microelectronic Circuits: includes CD-ROM (The Oxford Series in Electrical and Computer Engineering)','{"Adel S. Sedra", " Kenneth C. Smith"}','Oxford University Press, USA',2003,16, 12.01, 'hardcover', 'Foo', '{"Microelectronic", "Circuits:", "includes", "CD-ROM", "(The", "Oxford", "Series", "in", "Electrical", "and", "Computer", "Engineering)"}'),
    ('9780136019695','Feedback Control of Dynamic Systems','{"Gene F. Franklin", " J. David Powell", " Abbas Emami-Naeini"}','Prentice Hall',2009,18, 57.12, 'hardcover', 'Foo', '{"Feedback", "Control", "of", "Dynamic", "Systems"}'),
    ('9780132139311','Fundamentals of Applied Electromagnetics','{"Fawwaz T. Ulaby", " Eric Michielssen", " Umberto Ravaioli"}','Prentice Hall',2010,59, 83.39, 'hardcover', 'Foo', '{"Fundamentals", "of", "Applied", "Electromagnetics"}'),
    ('9780471272137','The Analysis and Design of Linear Circuits','{"Roland E. Thomas", " Albert J. Rosa"}','Wiley',2003,58, 64.6, 'hardcover', 'Foo', '{"The", "Analysis", "and", "Design", "of", "Linear", "Circuits"}'),
    ('9780471487289','Basic Engineering Circuit Analysis','{"J. David Irwin", " R. Mark Nelms"}','John Wiley & Sons',2004,49, 39.12, 'hardcover', 'Foo', '{"Basic", "Engineering", "Circuit", "Analysis"}'),
    ('9780201895520','Mechanics of Materials','{"Anthony M. Bedford", " Kenneth M. Liechti"}','Prentice Hall ',2000,89, 77.27, 'softcover', 'Foo', '{"Mechanics", "of", "Materials"}'),
    ('9780201000085','Fundamentals of Solar Energy Conversion (Addison-Wesley series in mechanics and thermodynamics)','{"Elmer E. Anderson"}','Addison Wesley Longman Publishing Co ',1982,42, 57.64, 'hardcover', 'Foo', '{"Fundamentals", "of", "Solar", "Energy", "Conversion", "(Addison-Wesley", "series", "in", "mechanics", "and", "thermodynamics)"}'),
    ('9780471457282','Fundamentals of Heat and Mass Transfer','{"Frank P. Incropera", " David P. DeWitt", " Theodore L. Bergman", " Adrienne S. Lavine"}','Wiley',2006,55, 35.42, 'hardcover', 'Foo', '{"Fundamentals", "of", "Heat", "and", "Mass", "Transfer"}'),
    ('9780136077916','Engineering Mechanics: Dynamics (12th Edition)','{"Russell C. Hibbeler"}','Prentice Hall',2009,53, 69.32, 'hardcover', 'Foo', '{"Engineering", "Mechanics:", "Dynamics", "(12th", "Edition)"}'),
    ('9780073529288','Shigley s Mechanical Engineering Design (Mcgraw-Hill Series in Mechanical Engineering)','{"Richard Budynas", " Keith Nisbett"}','McGraw-Hill Science/Engineering/Math',2010,47, 93.33, 'hardcover', 'Foo', '{"Shigley", "s", "Mechanical", "Engineering", "Design", "(Mcgraw-Hill", "Series", "in", "Mechanical", "Engineering)"}'),
    ('9780073529387','Mechanics of Materials','{"Ferdinand P. Beer", " E. Russell Johnston", " John T. Dewolf", " David F. Mazurek"}','McGraw-Hill Higher Education',2009,61, 65.32, 'hardcover', 'Foo', '{"Mechanics", "of", "Materials"}'),
    ('9780077366742','Thermodynamics: An Engineering Approach with Student Resources DVD','{"Yunus Cengel", " Michael Boles"}','McGraw-Hill Science/Engineering/Math',2010,2, 21.78, 'hardcover', 'Foo', '{"Thermodynamics:", "An", "Engineering", "Approach", "with", "Student", "Resources", "DVD"}'),
    ('9780136091837','Statics Study Pack for Engineering Mechanics','{"Russell C. Hibbeler"}','Prentice Hall',2009,65, 7.68, 'softcover', 'Foo', '{"Statics", "Study", "Pack", "for", "Engineering", "Mechanics"}'),
    ('9780470547410','Theory and Design for Mechanical Measurements','{"Richard S. Figliola", " Donald E. Beasley"}','Wiley',2010,45, 79.67, 'hardcover', 'Foo', '{"Theory", "and", "Design", "for", "Mechanical", "Measurements"}'),
    ('9780471410775','Transport Phenomena','{"R. Byron Bird", " Warren E. Stewart", " Edwin N. Lightfoot"}','Wiley',2001,94, 26.54, 'hardcover', 'Foo', '{"Transport", "Phenomena"}'),
    ('9781879335639','Five Hundred and Seven Mechanical Movements: Embracing All Those Which Are Most Important in Dynamics, Hydraulics, Hydrostatics, Pneumatics, Steam Engines...','{"Henry T. Brown"}','Astragal Press ',1995,74, 79.26, 'softcover', 'Foo', '{"Five", "Hundred", "and", "Seven", "Mechanical", "Movements:", "Embracing", "All", "Those", "Which", "Are", "Most", "Important", "in", "Dynamics,", "Hydraulics,", "Hydrostatics,", "Pneumatics,", "Steam", "Engines..."}'),
    ('9780073401065','Numerical Methods for Engineers, Sixth Edition','{"Steven Chapra", " Raymond Canale"}','McGraw-Hill Science/Engineering/Math',2009,97, 8.44, 'hardcover', 'Foo', '{"Numerical", "Methods", "for", "Engineers,", "Sixth", "Edition"}'),
    ('9780201824988','Introduction to Nuclear Engineering (3rd Edition)','{"John R. Lamarsh", " Anthony J. Baratta"}','Prentice Hall',2001,60, 55.34, 'hardcover', 'Foo', '{"Introduction", "to", "Nuclear", "Engineering", "(3rd", "Edition)"}'),
    ('9780824708344','Fundamentals of Nuclear Science and Engineering','{"J. Kenneth Shultis", " Richard E. Faw"}','CRC Press',2002,13, 57.49, 'hardcover', 'Foo', '{"Fundamentals", "of", "Nuclear", "Science", "and", "Engineering"}'),
    ('9781439808870','Nuclear Systems Volume I: Thermal Hydraulic Fundamentals, Second edition','{"Neil E. Todreas", " Mujid Kazimi"}','Taylor & Francis',2011,74, 2.68, 'hardcover', 'Foo', '{"Nuclear", "Systems", "Volume", "I:", "Thermal", "Hydraulic", "Fundamentals,", "Second", "edition"}'),
    ('9780471223634','Nuclear Reactor Analysis','{"James J. Duderstadt", " Louis J. Hamilton"}','Wiley',1976,82, 9.07, 'softcover', 'Foo', '{"Nuclear", "Reactor", "Analysis"}'),
    ('9780123736222','Nuclear Energy in the 21st Century: World Nuclear University Press','{"Ian Hore-Lacy"}','Academic Press',2006,66, 74.81, 'softcover', 'Foo', '{"Nuclear", "Energy", "in", "the", "21st", "Century:", "World", "Nuclear", "University", "Press"}'),
    ('9780387207780','Nuclear Energy: Principles, Practices, and Prospects','{"David Bodansky"}','Springer',2004,76, 9.6, 'hardcover', 'Foo', '{"Nuclear", "Energy:", "Principles,", "Practices,", "and", "Prospects"}'),
    ('9780415917711','The Tainted Desert: Environmental and Social Ruin in the American West','{"Valerie L. Kuletz"}','Routledge',1998,88, 93.76, 'softcover', 'Foo', '{"The", "Tainted", "Desert:", "Environmental", "and", "Social", "Ruin", "in", "the", "American", "West"}'),
    ('9789812567444','Introduction to Nuclear And Particle Physics: Solutions Manual for Second Edition of Text by Das and Ferbel','{"C. Bromberg", " A Das", " T Ferbel"}','World Scientific Publishing Company',2006,64, 48.39, 'softcover', 'Foo', '{"Introduction", "to", "Nuclear", "And", "Particle", "Physics:", "Solutions", "Manual", "for", "Second", "Edition", "of", "Text", "by", "Das", "and", "Ferbel"}'),
    ('9783540494713','Fundamentals of Radiation Materials Science: Metals and Alloys','{"Gary S. Was"}','Springer',2007,10, 22.64, 'hardcover', 'Foo', '{"Fundamentals", "of", "Radiation", "Materials", "Science:", "Metals", "and", "Alloys"}'),
    ('9780471531395','Fire from Ice: Searching for the Truth Behind the Cold Fusion Furor (Wiley Science Editions)','{"Eugene J. Mallove"}','John Wiley & Sons Inc',1991,26, 86.25, 'hardcover', 'Foo', '{"Fire", "from", "Ice:", "Searching", "for", "the", "Truth", "Behind", "the", "Cold", "Fusion", "Furor", "(Wiley", "Science", "Editions)"}'),
    ('9780387499826','Radiation Protection and Dosimetry: An Introduction to Health Physics','{"Michael G. Stabin"}','Springer',2007,22, 93.25, 'hardcover', 'Foo', '{"Radiation", "Protection", "and", "Dosimetry:", "An", "Introduction", "to", "Health", "Physics"}'),
    ('9780760011805','Information Technology Project Management','{"Kathy Schwalbe"}','Course Technology',1999,17, 59.93, 'softcover', 'Foo', '{"Information", "Technology", "Project", "Management"}'),
    ('9780470278703','Project Management: A Systems Approach to Planning, Scheduling, and Controlling','{"Harold Kerzner"}','Wiley',2009,46, 76.19, 'hardcover', 'Foo', '{"Project", "Management:", "A", "Systems", "Approach", "to", "Planning,", "Scheduling,", "and", "Controlling"}'),
    ('9780470169902','Design and Analysis of Experiments: MINITAB Companion','{"Douglas C. Montgomery", " Scott M. Kowalski"}','Wiley',2010,2, 97.49, 'softcover', 'Foo', '{"Design", "and", "Analysis", "of", "Experiments:", "MINITAB", "Companion"}'),
    ('9780735623057','Microsoft Office Project 2007 Step by Step (Step By Step (Microsoft))','{"Carl Chatfield", " Timothy Johnson D."}','Microsoft Press ',2007,57, 41.29, 'softcover', 'Foo', '{"Microsoft", "Office", "Project", "2007", "Step", "by", "Step", "(Step", "By", "Step", "(Microsoft))"}'),
    ('9780072392654','Applied Numerical Methods with MATLAB for Engineers and Scientists','{"Steven C. Chapra"}','McGraw-Hill Science/Engineering/Math',2004,1, 94.87, 'hardcover', 'Foo', '{"Applied", "Numerical", "Methods", "with", "MATLAB", "for", "Engineers", "and", "Scientists"}'),
    ('9780471635321','Principles of Highway Engineering and Traffic Analysis','{"Fred L. Mannering", " Walter P. Kilareski"}','John Wiley & Sons Inc ',1990,58, 5.87, 'softcover', 'Foo', '{"Principles", "of", "Highway", "Engineering", "and", "Traffic", "Analysis"}'),
    ('9780470053041','Applied Statistics and Probability for Engineers','{"Douglas C. Montgomery", " George C. Runger"}','Wiley',2010,44, 62.53, 'hardcover', 'Foo', '{"Applied", "Statistics", "and", "Probability", "for", "Engineers"}'),
    ('9780470467008','Fundamentals of Modern Manufacturing: Materials, Processes, and Systems','{"Mikell P. Groover"}','Wiley',2010,8, 88.32, 'hardcover', 'Foo', '{"Fundamentals", "of", "Modern", "Manufacturing:", "Materials,", "Processes,", "and", "Systems"}'),
    ('9780072471465','Product Design and Development','{"Karl Ulrich", " Steven Eppinger"}','McGraw-Hill/Irwin',2003,26, 98.34, 'hardcover', 'Foo', '{"Product", "Design", "and", "Development"}'),
    ('9780195168075','Engineering Economic Analysis','{"Donald G. Newnan", " Ted G. Eschenbach", " Jerome P. Lavelle"}','Oxford University Press, USA',2004,99, 89.04, 'hardcover', 'Foo', '{"Engineering", "Economic", "Analysis"}'),
    ('9780073376332','Statistics for Engineers and Scientists','{"William Navidi"}','McGraw-Hill Science/Engineering/Math',2010,26, 59.79, 'hardcover', 'Foo', '{"Statistics", "for", "Engineers", "and", "Scientists"}'),
    ('9780470169926','Introduction to Statistical Quality Control','{"Douglas C. Montgomery"}','Wiley',2008,60, 19.82, 'hardcover', 'Foo', '{"Introduction", "to", "Statistical", "Quality", "Control"}')
    """
)

delete_books = text(
    'DELETE FROM book'
)

insert_reviews = text(
    """INSERT INTO review ("ISBN", username, score, description, date) VALUES
    ('9780321197849', 'user1', 9, 'Very Informative like MeiHui', CURRENT_DATE)"""
)

delete_reviews = text(
    'DELETE FROM review'
)

delete_orders = text(
    'DELETE FROM "order"'
)

delete_books_orders = text(
    'DELETE FROM books_orders'
)

insert_feedbacks = text(
    """INSERT INTO feedback (customer_feedback, rating, customer_review, "ISBN") VALUES
    ('user2', 2, 'user1', '9780321197849')"""
)

delete_feedbacks = text(
    'DELETE FROM feedback'
)

def run():
    db.engine.execute(insert_customer)
    db.engine.execute(insert_store_manager)
    db.engine.execute(insert_books)
    db.engine.execute(insert_reviews)
    db.engine.execute(insert_feedbacks)

def clear():
    db.engine.execute(delete_books_orders)
    db.engine.execute(delete_orders)
    db.engine.execute(delete_feedbacks)
    db.engine.execute(delete_reviews)
    db.engine.execute(delete_books)
    db.engine.execute(delete_customer)
    db.engine.execute(delete_store_manager)
