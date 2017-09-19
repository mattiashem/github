from github import Github

g = Github("", "")

#for repo in g.get_user().get_repos():
#    print repo.name
#    #repo.edit(has_wiki=False)

org = g.get_organization('elino-apps')


#repo = org.create_repo('mattes', description='mattes test', homepage='http://apps.elino.se', private=False, has_issues=False, has_wiki=False, auto_init=False)
#team = org.create_team('Elino5')
team  = org.get_teams()
for t in team:
	print(t)

elino = org.get_team(5)
elino.add_to_members('hem')
