import os
import json

# ファイルパス
event_data_path = os.environ['GITHUB_EVENT_PATH']
print(f'Event data path: {event_data_path}')

# イベントデータの読み込み
with open(event_data_path, 'r') as f:
    event_data = json.load(f)

print(f'Event data: {json.dumps(event_data, indent=2)}')

# Issue情報の取得
issues = [event_data['issue']]
print(f'Issues: {json.dumps(issues, indent=2)}')

# README.mdの読み込み
with open('README.md', 'r') as f:
    readme_content = f.read()

# Issueリストの生成
issue_list = [f"- [{issue['title']}]({issue['html_url']})" for issue in issues]

# README.mdの更新
readme_content = readme_content.replace('<!-- ISSUE_LIST_START -->\n<!-- This section will be automatically updated by the GitHub Action -->\n<!-- ISSUE_LIST_END -->', '<!-- ISSUE_LIST_START -->\n{}\n<!-- ISSUE_LIST_END -->'.format('\n'.join(issue_list)))

# 更新内容を書き込み
with open('README.md', 'w') as f:
    f.write(readme_content)

print('README.md updated with the latest issues.')
