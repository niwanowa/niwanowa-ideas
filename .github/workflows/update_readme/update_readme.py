import os
import json
import datetime

# 環境変数をからREPOSITORYを取得
repository = os.environ.get('REPOSITORY')

# repositoryから、githubAPIを用いてIssueのリストを取得
issues = json.loads(os.popen(f'curl -s https://api.github.com/repos/{repository}/issues').read())

# README.mdの読み込み
with open('../../../README.md', 'r') as f:
    readme_content = f.read()

# Issueリストの生成
issue_list = [f"- [{issue['title']}]({issue['html_url']})" for issue in issues]
# Issueリストの最後に現在時刻を追加
issue_list.append(f"<!-- github actions: Updated on {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z')}-->")
print('----------------')
print(issue_list)

# README.mdの更新
# <!-- ISSUE_LIST_START --> と <!-- ISSUE_LIST_END --> の間を削除して、新しいIssueリストを挿入
readme_content = readme_content.split('<!-- ISSUE_LIST_START -->')[0] + '<!-- ISSUE_LIST_START -->\n' + '\n'.join(issue_list) + '\n<!-- ISSUE_LIST_END -->' + readme_content.split('<!-- ISSUE_LIST_END -->')[1]

# 更新内容を書き込み
with open('../../../README.md', 'w') as f:
    f.write(readme_content)

print('README.md updated with the latest issues.')
