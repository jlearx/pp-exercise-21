'''
Created on Aug 31, 2017

@author: jlearx
'''
 
def LoadData():
    data = ["Trump and DeVos fuel a for-profit college comeback\n",
"U.S. employers struggle to match workers with open jobs\n",
"Many L.A. students get to college; only a few finish\n",
"Uber will stop tracking riders after they are dropped off\n",
"Home health care: Shouldn’t it be work worth doing?\n",
"35 % of Americans are enrolled in auto pay — and It’s news to them\n",
"3 myths that could tank your credit score\n",
"The FCC moved to undo net neutrality. So what’s next?\n",
"Here’s what you need to know about flood insurance\n",
"Making sure your help gets to Hurricane Harvey’s victims\n",
"The Trump administration’s ongoing attack on workers\n",
"As bitcoin surges in price and popularity, so do the complaints\n",
"Harvey’s effects on fuel network hit U.S. motorists as gas prices rise\n",
"HUD tightens requirements for loans seniors can take against homes\n",
"Harvey’s burdens will fall hardest on the poor\n",
"Extreme vetting for 2 categories of green card applicants starting in Oct (Chinese)\n",
"File Harvey claims before law change\n",
"How parents can help their grown child get an apartment\n",
"Meet the sometime streamer\n",
"How to file a claim for flood damage\n",
"Gas prices increased 25 cents per gallon - a repercussion after Hurricane Harvey hit Texas (Chinese)\n",
"Donations came timely for Red Cross for victims of Hurricane Harvey (Chinese)\n",
"Unemployment in black and white\n",
"Delays in federal background checks leave more than 700,000 people in limbo\n",
"How Whole Foods’ lower prices will affect you\n",
"Here’s what health care will cost you in retirement\n",
"How Hurricane Harvey will impact prices at the gas pump\n",
"Will Uncle Sam pay your bills? Don’t fall for it\n",
"Looking beyond the Obamacare debate to improve health care\n",
"‘free cruise’ call could get you $900 (Chinese)\n",
"Beware of phone fraud - overseas callers also prosecuted by the US (Chinese)\n",
"Amazon cuts Whole Food prices in clear signal of changes to come\n",
"How to balance debt and investing\n",
"Why you should skip adderall as a study drug\n",
"Stay-at-home parents: Go back to work when your nest is empty\n",
"Loan servicer overcharged student borrowers eligible for debt forgiveness\n",
"How Netflix guesses what you want to watch\n",
"More debt relief for former Corinthian College students\n",
"4 ways companies track you online\n",
"Walmart and Google are plotting to change your shopping habits\n",
"Mr. Trump sides with Wall Street; you lose\n",
"Richard Cordray defends CFPB arbitration rule\n",
"How Powerball manipulated the odds to make another massive jackpot\n",
"How to buy the mattress that’s perfect for you\n",
"Talc powder causes cancer - patient awarded $417 million compensation (Chinese)\n",
"Robocalls bombarded SoCal residents (Chinese)\n",
"Let consumers sue companies\n",
"FBI warns of spreading W-2 email theft scheme\n",
"Aging parents with lots of stuff, and children who don’t want it\n",
"Trump moves to impede consumer lawsuits against nursing homes\n",
"Student loan debt crushing older Americans too\n",
"How to take care of your clothes\n",
"California 2017 final legislative session focused on five major issues (Chinese)\n",
"Labor groups step up pressure on Trump to deliver\n",
"Crowded TV marketplace gets ready for three tech giants\n",
"Could you live off Social Security alone?\n",
"Five new rights Congress could create for airplane passengers\n",
"Consumer Action staff gave talk on consumer rights and vocational schools guidelines (Chinese)\n",
"Wells Fargo troubles shift from phony bank accounts to real ones\n",
"Mylan finalizes $465 million EpiPen settlement with Justice Department (Chinese)\n",
"Americans are buying more food at Walmart\n",
"Former Corinthian students will get debt relief\n",
"Are you plagued by a serial get-out-of-debt disorder?\n",
"FDA halted implementation of calorie labeling rule (Chinese)\n",
"Texan’s LINE account been hacked (Chinese)\n",
"Taiwan Red Cross committed fraud in misusing donation accounts (Chinese)\n",
"Comcast $10M improper charges-case moved forward (Chinese)\n",
"Five things Wells Fargo account victims should do\n",
"How to make your house a smart home\n",
"Five major differences between federal and private student loans\n",
"Job seekers became victims of ‘recruitment scam’\n",
"New online scam targets tax preparers\n",
"Zillow says consumer agency is threatening legal action over its ads\n",
"Downpayment and closing-cost help for low-income homebuyers\n",
"Is LinkedIn trying to protect your data — or hoard it?\n",
"Trump’s plan of tax reform might sink the real estate market (Chinese)\n",
"Don’t mess with contact lens consumer rights\n",
"Drug companies growing less generous in helping patients pay for meds\n",
"As prices rise, mortgage lenders make it easier to buy a house\n",
"Freedom from cable isn’t free\n",
"The whys of increasing inequality: A graphical portrait\n",
"Six foods that marketers want you to think are healthy\n",
"How a conservative TV giant is ridding itself of regulation\n",
"Heatlh insurers get more time to calculate 2018 increases\n",
"Two online security steps you should stop putting off\n",
"Beware of malicious software - take caution when opening emails (Chinese)\n",
"Consumer debt is at a record high. Haven’t we learned?\n",
"Facebook Watch is company’s new plan for online video\n",
"Trump officials begin review of Obama emissions standards\n",
"Major rental-home companies set to merge\n",
"Trump’s immigration reform plan has pros and cons (Chinese)\n",
"The costs of deferring your student loans\n",
"Heart and asthma monitors? There’s an app for that\n",
"Fannie and Freddie will stick with FICO formula\n",
"Closing the courthouse door\n",
"2 Senators question effects of a reverse mortgage proposal\n",
"Chips can fall out of credit cards, leaving consumers vulnerable\n",
"Millennials: Don’t fear the market\n",
"Wells Fargo, awash in scandal, faces violations over car insurance refunds\n",
"Why can’t Americans ditch checks?\n"]
    return data

if __name__ == '__main__':
    data = LoadData()
    filePath = "../"
    
    filename = input("Please enter the desired file name: ")
    
    print("Writing data to file " + filename + " ...",end='')
    
    with open(filePath + filename, 'w') as open_file:
        open_file.writelines(data)
    
    print("Done!")