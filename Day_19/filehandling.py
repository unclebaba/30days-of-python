## Write a function which count number of lines and number of words in a text. 
# All the files are in the data the folder: 
# a) Read obama_speech.txt file and count number of lines and words 
# b) Read michelle_obama_speech.txt file and count number of lines and words 
# c) Read donald_speech.txt file and count number of lines and words
# d) Read melina_trump_speech.txt file and count number of lines and words
#A
def count_lines_and_words(text):
    lines = text.split('\n')
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    return num_lines, num_words
text = "My fellow citizens:...\n...passed on from generation to generation: the God-given promise that all are equal, all are free, and all deserve a chance to pursue their full measure of happiness."
num_lines, num_words = count_lines_and_words(text)
print(f"Number of lines: {num_lines}")
print(f"Number of words: {num_words}")

#B.
def count_lines_words(text):
    lines = text.split('\n')
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    return num_lines, num_words
text = "As you might imagine, for Barack, running for president is nothing compared to that first game of basketball with my brother, Craig.\n\nI can't tell you how much it means to have Craig and my mom here tonight. Like Craig, I can feel my dad looking down on us, just as I've felt his presence in every grace-filled moment of my life.\n\nAt 6-foot-6, I've often felt like Craig was looking down on me too ... literally. But the truth is, both when we were kids and today, he wasn't looking down on me. He was watching over me.\n\nAnd he's been there for me every step of the way since that clear February day 19 months ago, when — with little more than our faith in each other and a hunger for change — we joined my husband, Barack Obama, on the improbable journey that's brought us to this moment.\n\nBut each of us also comes here tonight by way of our own improbable journey."

num_lines, num_words = count_lines_words(text)
print(f"Number of lines: {num_lines}")
print(f"Number of words: {num_words}")

#C.

def count_lines_words(text):
    lines = len(text.split('\n'))
    words = len(text.split())
    return lines, words
text = "Chief Justice Roberts, President Carter, President Clinton,President Bush, fellow Americans and people of the world – thank you. We the citizens of America have now joined a great national effort to rebuild our county and restore its promise for all our people. Together we will determine the course of America for many, many years to come. Together we will face challenges. We will confront hardships. But we will get the job done. Every four years we gather on these steps to carry out the orderly and peaceful transfer of power. And we are grateful to President Obama and First Lady Michelle Obama for their gracious aid throughout this transition. They have been magnificent, thank you. Today’s ceremony, however, has very special meaning because today we are not merely transferring power from one administration to another – but transferring it from Washington DC and giving it back to you the people. For too long a small group in our nation’s capital has reaped the rewards of government while the people have borne the cost. Washington flourished but the people did not share in its wealth. Politicians prospered but the jobs left and the factories closed.The establishment protected itself but not the citizens of our country. Their victories have not been your victories. Their triumphs have not been your triumphs. While they have celebrated there has been little to celebrate for struggling families all across our land. That all changes starting right here and right now because this moment is your moment. It belongs to you. It belongs to everyone gathered here today and everyone watching all across America today. This is your day.This is your celebration.And this – the United States of America – is your country.What truly matters is not what party controls our government but that this government is controlled by the people. Today, January 20 2017, will be remembered as the day the people became the rulers of this nation again.The forgotten men and women of our country will be forgotten no longer. Everyone is listening to you now. You came by the tens of millions to become part of a historic movement – the likes of which the world has never seen before. At the centre of this movement is a crucial conviction – that a nation exists to serve its citizens.Americans want great schools for their children, safe neighbourhoods for their families and good jobs for themselves. These are just and reasonable demands.Mothers and children trapped in poverty in our inner cities, rusted out factories scattered like tombstones across the landscape of our nation. An education system flushed with cash, but which leaves our young and beautiful students deprived of all knowledge. And the crime and the gangs and the drugs which deprive people of so much unrealised potential. We are one nation, and their pain is our pain, their dreams are our dreams, we share one nation, one home and one glorious destiny. Today I take an oath of allegiance to all Americans. For many decades, we’ve enriched foreign industry at the expense of American industry, subsidised the armies of other countries, while allowing the sad depletion of our own military. We've defended other nations’ borders while refusing to defend our own.And spent trillions and trillions of dollars overseas while America’s infrastructure has fallen into disrepair and decay. We have made other countries rich while the wealth, strength and confidence of our country has dissipated over the horizon. One by one, shutters have closed on our factories without even a thought about the millions and millions of those who have been left behind. But that is the past and now we"
print(f"Number of lines: {num_lines}")
print(f"Number of words: {num_words}")

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages


