from collections import namedtuple

Repository = namedtuple('Repository', (
    'id',
    'owner',
    'name',
    'full_name',
    'description',
    'private',
    'fork',
    'url',
    'html_url',
    'archive_url',
    'assignees_url',
    'blobs_url',
    'branches_url',
    'clone_url',
    'collaborators_url',
    'comments_url',
    'commits_url',
    'compare_url',
    'contents_url',
    'contributors_url',
    'deployments_url',
    'downloads_url',
    'events_url',
    'forks_url',
    'git_commits_url',
    'git_refs_url',
    'git_tags_url',
    'git_url',
    'hooks_url',
    'issue_comment_url',
    'issue_events_url',
    'issues_url',
    'keys_url',
    'labels_url',
    'languages_url',
    'merges_url',
    'milestones_url',
    'mirror_url',
    'notifications_url',
    'pulls_url',
    'releases_url',
    'ssh_url',
    'stargazers_url',
    'statuses_url',
    'subscribers_url',
    'subscription_url',
    'svn_url',
    'tags_url',
    'teams_url',
    'trees_url',
    'homepage',
    'language',
    'forks_count',
    'stargazers_count',
    'watchers_count',
    'size',
    'default_branch',
    'open_issues_count',
    'has_issues',
    'has_wiki',
    'has_pages',
    'has_downloads',
    'pushed_at',
    'created_at',
    'updated_at',
    'permissions',
    'subscribers_count',
    'organization',
    'parent',
    'source',
    'network_count',
    'watchers',
    'open_issues',
    'forks',
    ))

User = namedtuple('User', (
    'login',
    'id',
    'avatar_url',
    'gravatar_id',
    'url',
    'html_url',
    'followers_url',
    'following_url',
    'gists_url',
    'starred_url',
    'subscriptions_url',
    'organizations_url',
    'repos_url',
    'events_url',
    'received_events_url',
    'type',
    'site_admin',
    'name',
    'company',
    'blog',
    'location',
    'email',
    'hireable',
    'bio',
    'public_repos',
    'public_gists',
    'followers',
    'following',
    'created_at',
    'updated_at',
    ))

PullRequest = namedtuple('PullRequest', (
    'id',
    'url',
    'html_url',
    'diff_url',
    'patch_url',
    'issue_url',
    'commits_url',
    'review_comments_url',
    'review_comment_url',
    'comments_url',
    'statuses_url',
    'number',
    'state',
    'title',
    'body',
    'assignee',
    'milestone',
    'locked',
    'created_at',
    'updated_at',
    'closed_at',
    'merged_at',
    'head',
    'base',
    '_links',
    'user',
    'merge_commit_sha',
    'merged',
    'mergeable',
    'merged_by',
    'comments',
    'commits',
    'additions',
    'deletions',
    'changed_files',
))
