from git import Repo

#PATH_OF_GIT_REPO = r'path\to\your\project\folder\.git'
PATH_OF_GIT_REPO = './Trinhvn82/backup-DB.git'
  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():
#    try:
#    repo = Repo(PATH_OF_GIT_REPO)
    repo = Repo('tmp\.git')
    repo.index.add(['*'])
    #repo.git.add(update=True)
    repo.index.commit(COMMIT_MESSAGE)
    origin = repo.remote(name='origin')
    origin.push()

# from git import Repo
# repo = Repo('path/to/git/repo')  # if repo is CWD just do '.'

# repo.index.add(['*'])
# repo.index.commit('my commit description')
# origin = repo.remote('origin')
# origin.push()

#    except Exception as e:
#        print(str(e))    

git_push()
