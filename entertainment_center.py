import media
import fresh_tomatoes


# Creating instances of the class Movie 
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


shawshank_redemption = media.Movie("Shawshank Redemption",
                                   "A story of a man who planned his redemption from prison for years without any body noticing",
                                   "http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")
                                

Concussion = media.Movie("Concussion",
                         "A doctor discovers that american football has caused brain damage to many player and initiated a battle to protect players",
                         "http://t0.gstatic.com/images?q=tbn:ANd9GcQNcKK3F0CNa4D2APk5shk73A_Jym89iZzlosXbCFtCpC9tVSaf",
                         "https://www.youtube.com/watch?v=Qk-1TLVUPZk")

Pompie = media.Movie("Pompie",
                     "A sotry that takes place in the ancient ciy of Pompie which was destroyed by a volacano",
                     "http://t1.gstatic.com/images?q=tbn:ANd9GcQUnlHZqtldOWcTA5G5zf75oLNbhc8pJdEx9UadPR5QPjR3nHvy",
                     "https://www.youtube.com/watch?v=t6TRwfxDICM")


Seperation = media.Movie("Seperation",
                         "The story of a couple during their seperation while dealing with a father with alzheimer and a small daughter",
                         "http://t0.gstatic.com/images?q=tbn:ANd9GcR5z7IfhuXWgtFA6Xuopouyl_mFfetECy87P0z11ojjHD5PcHs8",
                         "https://www.youtube.com/watch?v=nwEgDPPATy0")

steve_jobs = media.Movie("Steve Jobs",
                         "The film covers the personal life of Steve Jobs and how he managed to bring Apple to what it became",
                         "http://t3.gstatic.com/images?q=tbn:ANd9GcSWuhJZosAINTA9iDAmdVUSEJGCXsyckZEdHvVPp76wvPmVY0rN",
                         "https://www.youtube.com/watch?v=aEr6K1bwIVs")


# Adding the instances (movies) to a list 
movies= [toy_story, shawshank_redemption, Concussion, Pompie, Seperation, steve_jobs]

# Opening the web page using a function defined in the imported fresh_tomatoes file
fresh_tomatoes.open_movies_page(movies)
