class Voter:
  #must handle duplicate ids
  voterInfo = {}
  vote_counter = {}
  validPosts = ["President", "Vice President", "Secretary", "Treasurer"]
  def __init__(self, student_id, name):
    if student_id not in Voter.voterInfo:
      self.student_id = student_id
      self.name = name
      if student_id not in Voter.voterInfo:
        Voter.voterInfo[student_id] =  name
        self.VotedFor = set()
    else:
      self.student_id = None
      self.name = None

  votes = {}
  voteCount = 0
  #must handle case if already voted
  def vote(self, candidate_id, post: str):
    if self.student_id in Voter.voterInfo and post in Candidate.candidateInfo and candidate_id in Candidate.candidateInfo[post]:
      t = self.VotedFor.copy()
      for votes in t:
        if votes[1] == post:
          Voter.vote_counter[votes] -= 1
          self.VotedFor.remove(votes)
          
      Voter.vote_counter[(candidate_id,post)] += 1
      self.VotedFor.add((candidate_id, post))
    
#     key = (candidate_id, post)
#     if key[0] not in votes:
#       votes[key] = 0
#     else:s
#       votes[key] += 1
    
    

  def get_candidates_by_post(self, post):
    self.post = post
    try:
      output = f"Following candidates are running for {post}:\n"
      for studentID in Candidate.candidateInfo[post]:
        output += f"Name: {Candidate.candidateInfo[post][studentID]}, Candidate_Id: {studentID}\n"
      output = output.strip("\n")
      return output
    except:
      pass
       
		       
    #print all the candidates and their info for all posts
    #This should be formatted in such a way that all candidates for a post should be displayed together
  def get_all_candidates(self):
      output_str = ""
      for el in Candidate.candidateInfo:
        output_str = output_str + self.get_candidates_by_post(el) + "\n\n"
      output_str =  output_str.strip()
      return output_str
    

class Candidate(Voter):
	#should handle duplicates
  candidateInfo = dict()
  lis = []
  def __init__(self, student_id, candidate_name,  posts):
    super().__init__(student_id, candidate_name)
    if not any ([student_id in el for el in (Candidate.candidateInfo).values()]):
      self.student_id = student_id
      self.candidate_name = candidate_name
      self.posts = posts
      for i in list(posts):
        Voter.vote_counter[(student_id,i)] = 0
    
      for post in posts:
        if post not in Candidate.candidateInfo:
              Candidate.candidateInfo[post] = dict()
              Candidate.candidateInfo[post][student_id] = candidate_name
        else:
              Candidate.candidateInfo[post][student_id] =candidate_name

    else:
      self.student_id = None
      self.candidate_name = None
      self.posts = None


  #output: return the following string
  # Hello Candidate @663 Norma Reader
  # Post: President, Votes: 1
  # Post: Vice President, Votes: 1
  #output ends here, no blank line
  	
	#see votes cast to the candidate across all the posts they are running for
  def see_votes(self):
    output = f"Hello Candidate @{self.student_id} {self.candidate_name}\n"
    for post in Candidate.candidateInfo.keys():
      if (self.student_id, post) in Voter.vote_counter:
        output += f'Post: {post}, Votes: {Voter.vote_counter[(self.student_id, post)]}\n'
    output.strip('\n')

    return output

    
    
    

	#feel free to remove this method if you feel like there is no need
# 	def vote(self, candidate_id):
#     self.candidate_id = candidate_id
#     if 
# 		pass


class Records:	
	#show all the candidates, their info and the posts they are running for this election
  @staticmethod
  def show_all_candidates():
    output_str = ""
    for el in Candidate.candidateInfo:
      output_str = output_str + Records.show_candidates_by_post(el) + "\n\n"
    output_str =  output_str.strip()
    return output_str
		

	#Shows all the candidates info if they are running for post
  @staticmethod
  def show_candidates_by_post(post):
    output = f"Following candidates are running for {post}\n"
    for studentID in Candidate.candidateInfo[post]:
        output += f"Name: {Candidate.candidateInfo[post][studentID]} Candidate_Id: {studentID}\n"
    output = output.strip()
    return output
	
	#show all the current votes of all the candidates
  @classmethod
  def show_all_tally(cls):
    output = ""
    for post in Candidate.candidateInfo:
      output += f"Running for {post}:\n"
      for studentID in Candidate.candidateInfo[post]:
        output += f"Name: {Candidate.candidateInfo[post][studentID]}, Candidate_Id: {studentID}, Votes:{Voter.vote_counter[(studentID, post)]}\n"
      output += '\n'
    output = output.strip()
    return output
   
    
    

	#returns winners across all the posts
  @classmethod
  def get_winners(cls):
    output = ""
    winner = []
    total = float('-inf')
    for post in Candidate.candidateInfo:
      output += f"Winner for {post}:\n"
      total = float('-inf')
      winner = []
      for studentID in Candidate.candidateInfo[post]:
        if Voter.vote_counter[(studentID, post)] > total:
          total = Voter.vote_counter[(studentID, post)]
          winner = [Candidate.candidateInfo[post][studentID], studentID]
      output += f"{winner[0]} @ {winner[1]} with {total} votes\n"
        
      output += '\n'
    output = output.strip()
    return output
    # Records.get_winner()
  # #output: return the following string
  # Winner for President:
  # Norma Reader @ 663 with 1 votes
  # #blank line
  # Winner for Vice President:
  # Norma Reader @ 663 with 1 votes

  # Winner for Treasurer:
  # Rocky Rodgers @ 949 with 0 votes

  # Winner for Secretary:
  # Rocky Rodgers @ 949 with 0 votes
  # #end of output; no blank line at the end  

    
    
    

	#set all the votes received by the candidates to 0.
  @staticmethod
  def reset_votes():
    for key in Voter.vote_counter:
      Voter.vote_counter[key] = 0



if __name__ == "__main__":
  #Please test your code here
  voter1  = Voter(440, 'Willie Pontiff')
  voter2  = Voter(863, 'Isaac Hix')
  voter3  = Voter(613, 'Rosemary Kane')
  voter4  = Voter(885, 'Charles Shumock')
  voter5  = Voter(863, 'Helen Ryan')

  #Since voter5 and voter2 have the same id, there will still be only 4 voters. So the max vote a candidate can have is 4

  candidate1  = Candidate(663, 'Norma Reader' , ["President", "Vice President"])
  candidate2  = Candidate(365, 'Elizabeth Riggs', ["Vice President"])
  candidate3  = Candidate(949, 'Rocky Rodgers', ["Treasurer", "Secretary"] )
  candidate4  = Candidate(949, 'Bill Musk', ["Vice President", "Secretary"] )

  #Similarly since candidate4 has the same id as candidate3, this object shouldn't be initialized

  (voter1.get_candidates_by_post("Vice President")) #return the output as a string, not print
  #output: 
  # Following candidates are running for Vice President:
  # Name: Norma Reader, Candidate_Id: 663
  # Name: Elizabeth Riggs, Candidate_Id: 365 
  #output string ends here, no blank line at the end

  (voter1.get_all_candidates())
  #output: returns the following string
  # Following candidates are running for President:
  # Name: Norma Reader, Candidate_Id: 663
  # #this one though is a blank line
  # Following candidates are running for Vice President:
  # Name: Norma Reader, Candidate_Id: 663
  # Name: Elizabeth Riggs, Candidate_Id: 365

  # Following candidates are running for Treasurer:
  # Name: Rocky Rodgers, Candidate_Id: 949

  # Following candidates are running for Secretary:
  # Name: Rocky Rodgers, Candidate_Id: 949
  #end of output; no blank line at the end  

  # .vote: (void) returns None
  voter1.vote(663, "President") #this is a valid vote since 663 is running for president
  candidate2.vote(863, "Treasurer") #this would be invalid since id 863 isn't running for any post
  voter2.vote(949, "President") #also invalid as 949 only running for Treasurer and Secretary
  voter2.vote(123, "Queen") #invalid because neither 123 is a candidate nor do we have any post for queen
  candidate2.vote(365, "Vice President") #valid
  candidate2.vote(663, "Vice President") #also valid
  #but now candidate2's vote updates and now goes not to 365 but to 663
  #You can only vote for a candidate(this doesn't mean you can only vote once) per post

  ((candidate1.see_votes()))
  #output: return the following string
  # Hello Candidate @663 Norma Reader
  # Post: President, Votes: 1
  # Post: Vice President, Votes: 1
  #output ends here, no blank line

  (candidate2.see_votes())
  #output: return the following string
  # Hello Candidate @365 Elizabeth Riggs
  # Post: Vice President, Votes: 0
  (Records.show_all_candidates())
  # print((Records.show_all_tally()))
  # print(Records.get_winners())
  #output: return the following string
  # Running for President:
  # Name: Norma Reader, Candidate_Id: 663, Votes: 1
  # #blank line
  # Running for Vice President:
  # Name: Norma Reader, Candidate_Id: 663, Votes: 1
  # Name: Elizabeth Riggs, Candidate_Id: 365, Votes: 0

  # Running for Treasurer:
  # Name: Rocky Rodgers, Candidate_Id: 949, Votes: 0

  # Running for Secretary:
  # Name: Rocky Rodgers, Candidate_Id: 949, Votes: 0
  # #end of output; no blank line at the end  

  print(Records.get_winners())
  
  # #output: return the following string
  # Winner for President:
  # Norma Reader @ 663 with 1 votes
  # #blank line
  # Winner for Vice President:
  # Norma Reader @ 663 with 1 votes

  # Winner for Treasurer:
  # Rocky Rodgers @ 949 with 0 votes

  # Winner for Secretary:
  # Rocky Rodgers @ 949 with 0 votes
  # #end of output; no blank line at the end  

    
































