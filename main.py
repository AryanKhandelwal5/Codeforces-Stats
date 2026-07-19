import requests

username = input("Enter Your Codeforces Username: ")

url = f"https://codeforces.com/api/user.info?handles={username}&checkHistoricHandles=false"

print(f"Fetching data for user: {username}...\n")

ORANGE = '\033[38;2;255;165;0m'
RESET = '\033[0m'

try:
  response = requests.get(url) # GET Request
  data = response.json() 
  # print(data)  
  
  if(data['status'] == 'OK'):
    info = data['result'][0]
    print(ORANGE, end="")

    print(f"🏆 {info.get('rank','N/A').capitalize()}")
    
    print(f"👤 User Handle: {info.get('handle','N/A')} ")
    
    if(info.get('firstName') and info.get('lastName')):
      print(f"😎 User Name: {info.get('firstName','N/A')} {info.get('lastName','N/A')} ")

    if(info.get('organization') and info.get('country')):
      print(f"🏞️  From {info.get('organization','N/A')} , {info.get('country','N/A')} ")
    elif(info.get('organization')):
      print(f"🏞️  From {info.get('organization','N/A')} ")
    elif(info.get('country')):
      print(f"🏞️  From {info.get('country','N/A')} ")
    
    print(f"🔥 Contest rating: {info.get('rating','N/A')} (max. {info.get('maxRank','N/A').capitalize()}, {info.get('maxRating','N/A')})")  # Contest rating: 964 (max. pupil, 1215)
    
    print(f"👥 Friend of: {info.get('friendOfCount','N/A')} users")
    print(RESET, end="")
    
  else:
    print(f"❌ Error: {data.get('comment','N/A')}")

except Exception as e:
  print(f"Error fetching data: {e}")