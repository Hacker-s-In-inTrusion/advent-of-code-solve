#include <bits/stdc++.h>

using namespace std;

vector<string> height_map;
vector<int> basin;
int ans = 1;

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { -1, 0, 1, 0 };

bool visited[105][105];

int bfs(int x, int y, int len, int sz)
{
  int cnt = 0;
  queue<pair<int, int>> q;
  q.push(make_pair(x, y));
  visited[y][x] = true;

  while (!q.empty())
  {
    int x = q.front().first;
    int y = q.front().second;
    q.pop();
    cnt++;

    for (int i = 0; i < 4; i++)
    {
      int nx = x + dx[i];
      int ny = y + dy[i];

      if (nx < 0 || ny < 0 || nx >= len || ny >= sz)
        continue;

      if (!visited[ny][nx] && height_map[ny][nx] != '9')
      {
        q.push(make_pair(nx, ny));
        visited[ny][nx] = true;
      }
    }
  }

  return cnt;
}

int main(void)
{
  cin.tie(NULL);
  ios::sync_with_stdio(false);

  while(!cin.eof() && cin.good())
  {
    string s;
    cin >> s;
    height_map.push_back(s);
  }

  int sz = height_map.size() - 1;
  int len = height_map[0].length();

  for (int i = 0; i < sz; i++)
  {
    for (int j = 0; j < len; j++)
    {
      if (height_map[i][j] != '9' && !visited[i][j])
        basin.push_back(bfs(j, i, len, sz));
    }
  }

  sort(basin.begin(), basin.end(), greater<>());

  for (int i = 0; i < 3; i++)
    ans *= basin[i];

  cout << ans;

  return 0;
}