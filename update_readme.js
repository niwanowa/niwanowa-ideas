const fs = require('fs');

const issues = JSON.parse(process.env.GITHUB_EVENT_PATH);

let readmeContent = fs.readFileSync('README.md', 'utf-8');

const issueList = issues.map(issue => `- [${issue.title}](${issue.html_url})`);

readmeContent = readmeContent.replace(/<!-- ISSUE_LIST_START -->[\s\S]*<!-- ISSUE_LIST_END -->/, `<!-- ISSUE_LIST_START -->\n${issueList.join('\n')}\n<!-- ISSUE_LIST_END -->`);

fs.writeFileSync('README.md', readmeContent);

console.log('README.md updated with the latest issues.');
