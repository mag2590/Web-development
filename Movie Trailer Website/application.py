import videos
import fresh_tomatoes

harry_potter = videos.Movie("Harry Potter","Adaptation of the first of J.K. Rowling's popular children's novels about Harry Potter, a boy who learns on his eleventh birthday that he is the orphaned son of two powerful wizards and possesses unique magical powers of his own. He is summoned from his life as an unwanted child to become a student at Hogwarts, an English boarding school for wizards. There, he meets several friends who become his closest allies and help him discover the truth about his parents' mysterious deaths.",
    "images/harry_potter_and_the_sorcerers_stone_ver4.jpg","https://youtu.be/VyHV0BRtdxo")


lord_of_the_rings=videos.Movie("Lord of the rings","The future of civilization rests in the fate of the One Ring, which has been lost for centuries. Powerful forces are unrelenting in their search for it. But fate has placed it in the hands of a young Hobbit named Frodo Baggins (Elijah Wood), who inherits the Ring and steps into legend. A daunting task lies ahead for Frodo when he becomes the Ringbearer - to destroy the One Ring in the fires of Mount Doom where it was forged.","images/lord_of_the_rings.jpg","https://youtu.be/qyquczkXgPc")

saw  = videos.Movie("Saw","Photographer Adam Stanheight (Leigh Whannell) and oncologist Lawrence Gordon (Cary Elwes) regain consciousness while chained to pipes at either end of a filthy bathroom. As the two men realize they've been trapped by a sadistic serial killer nicknamed -Jigsaw and must complete his perverse puzzle to live, flashbacks relate the fates of his previous victims. Meanwhile, Dr. Gordon's wife (Monica Potter) and young daughter (Makenzie Vega) are forced to watch his torture via closed-circuit video.","images/saw.jpg","https://youtu.be/S-1QgOMQ-ls")

doctor_strange=videos.Movie("Doctor Strange","Dr. Stephen Strange's (Benedict Cumberbatch) life changes after a car accident robs him of the use of his hands. When traditional medicine fails him, he looks for healing, and hope, in a mysterious enclave. He quickly learns that the enclave is at the front line of a battle against unseen dark forces bent on destroying reality. Before long, Strange is forced to choose between his life of fortune and status or leave it all behind to defend the world as the most powerful sorcerer in existence.","images/doctor_strange.jpeg","https://youtu.be/Lt-U_t2pUHI")

pink_floyd_the_wall=videos.Movie("Pink Floyd: The Wall","In this visual riff on Pink Floyd's album ''The Wall,'' successful but drugged-out musician Pink (Bob Geldof) is looking back on his isolated childhood from the confines of a Los Angeles hotel room. Through a swirl of flashbacks and chemical-induced hallucinations, Pink recalls his lonely upbringing, during which he built a symbolic wall to the world as he coped with the death of his father (James Laurenson) and the overbearing ways of his mother (Christine Hargreaves).","images/the_wall.jpeg","https://youtu.be/ZIhW1XIAY9M")

hannibal = videos.Movie("Silence of the lambs","Jodie Foster stars as Clarice Starling, a top student at the FBI's training academy. Jack Crawford (Scott Glenn) wants Clarice to interview Dr. Hannibal Lecter (Anthony Hopkins), a brilliant psychiatrist who is also a violent psychopath, serving life behind bars for various acts of murder and cannibalism. Crawford believes that Lecter may have insight into a case and that Starling, as an attractive young woman, may be just the bait to draw him out.","images/hannibal.jpeg","https://youtu.be/LOfH7s__hMY")

movies=[harry_potter,lord_of_the_rings,saw,doctor_strange,pink_floyd_the_wall,
        hannibal]
fresh_tomatoes.open_movies_page(movies)