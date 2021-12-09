#include <bits/stdc++.h>

using namespace std;

vector<string> height_map;
int ans = 0;

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { -1, 0, 1, 0 };

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

  int sz = height_map.size();
  int len = height_map[0].length();

  for (int i = 0; i < sz; i++)
  {
    for (int j = 0; j < len; j++)
    {
      int cnt = 0;

      for (int k = 0; k < 4; k++)
      {
        int fx = j + dx[k];
        int fy = i + dy[k];

        if (fx < 0 || fy < 0 || fx >= len || fy >= sz)
          continue;

        if (height_map[i][j] < height_map[fy][fx])
          cnt++;
      }

      if (cnt == 4)
        ans += (height_map[i][j] - '0') + 1;

      else if (cnt == 3 && (i == 0 || i == sz - 1 || j == 0 || j == len - 1))
        ans += (height_map[i][j] - '0') + 1;

      else if (cnt == 2 && ((i == 0 && j == 0) || (i == 0 && j == len - 1) || (i == sz - 1 && j == 0) || (i == sz - 1 && j == len - 1)))
        ans += (height_map[i][j] - '0') + 1;
    }
  }

  cout << ans;

  return 0;
}