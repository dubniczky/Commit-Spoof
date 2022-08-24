import sys
from pathlib import Path
from git import Repo, Commit


def extract_users(repo, branch):
    commits = list(repo.iter_commits(branch))
    return list( set( [ (c.author.name, c.author.email) for c in commits ] ) )


def print_users(users):
    print(f'{len(users)} users found in repository.')
    print( '\n'.join([ f'{u[0]}:{u[1]}' for u in users ]) )


def get_branch_names(repo):
    return [ str(b) for b in repo.branches ]


def main():
    path = '.'
    if len(sys.argv) > 1:
        path = sys.argv[1]
    path = Path(path).resolve()
    print('Repository path:', path)

    repo = Repo(path)
    print('Branches:')
    branches = get_branch_names(repo)
    print(branches)
    
    users = extract_users(repo, 'main') 
    print_users(users)


if __name__ == '__main__':
    main()