import re

# test_str = '''


# John Carmack
# @ID_AA_Carmack
# Independent AI researcher, Consulting CTO Oculus VR, Founder Id Software and Armadillo Aerospace
# @arxivblog
# @arxivblog
# The best new ideas in science and technology. Now blogging at Discover Magazine, previously at Technology Review and Medium
# SpaceX
# @SpaceX
# SpaceX designs, manufactures and launches the world’s most advanced rockets and spacecraft
# Tim Urban
# @waitbutwhy
# Writer, infant
# TESLARATI
# @Teslarati
# Tesla, SpaceX, Elon Musk, and #FutureTech Go behind the scenes 
# @TeslaratiTeam
# Ashlee Vance
# @ashleevance

# '''

import re
p = re.compile(r'@([^\s:]+)')
# test_str = "@galaxy5univ I like you\nRT @BestOfGalaxies: Let's sit under the stars ...\n@jonghyun__bot .........((thanks)\nRT @yosizo: thanks.ddddd <https://y...content-available-to-author-only...o.com>\nRT @LDH_3_yui: #fam, ccccc https://m...content-available-to-author-only...s.com"
# print(p.findall(test_str)) 
# p2 = re.compile(r'(?:http|ftp|https)://(?:[\w_-]+(?:(?:\.[\w_-]+)+))(?:[\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?')
# print(p2.findall(test_str))
# # => ['galaxy5univ', 'BestOfGalaxies', 'jonghyun__bot', 'yosizo', 'LDH_3_yui']
# # => ['https://yahoo.com', 'https://msn.news.com']