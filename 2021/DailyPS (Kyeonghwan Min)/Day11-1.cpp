#include <bits/stdc++.h>

using namespace std;

int ans = 0;
int sz, len;

vector<string> octopus;
vector<int> g[15];

int dx[8] = { 0, 1, 1, 1, 0, -1, -1, -1 };
int dy[8] = { -1, -1, 0, 1, 1, 1, 0, -1 };

int catch_flashes(void)
{
  bool is_flashed[15][15] = { 0 };
  int ret = 0;

  for (int i = 0; i < sz; i++)
  {
    for (int j = 0; j < len; j++)
      g[i][j]++;
  }

  for (int i = 0; i < sz; i++)
  {
    for (int j = 0; j < len; j++)
      cout <<  g[i][j] << " ";

    cout << "\n";
  }

  cout << '\n';

  while (true)
  {
    int cnt = 0;

    for (int i = 0; i < sz; i++)
    {
      for (int j = 0; j < len; j++)
      {
        if (is_flashed[i][j])
          continue;

        if (g[i][j] > 9)
        {
          is_flashed[i][j] = true;

          for (int k = 0; k < 8; k++)
          {
            int nx = j + dx[k];
            int ny = i + dy[k];

            if (nx < 0 || nx >= len || ny < 0 || ny >= sz)
              continue;

            g[ny][nx]++;
          }

          cnt++;
        }
      }
    }

    if (!cnt)
      break;
  }
  
  

  for (int i = 0; i < sz; i++)
  {
    for (int j = 0; j < len; j++)
    {
      if (is_flashed[i][j])
      {
        ret++;
        g[i][j] = 0;
      }
    }
  }

  return ret;
}

int main(void)
{
  cin.tie(NULL);
  ios::sync_with_stdio(false);

  while(!cin.eof() && cin.good())
  {
    string s;
    cin >> s;

    octopus.push_back(s);
  }

  sz = octopus.size() - 1;
  len = octopus[0].length();

  for (int i = 0; i < sz; i++)
  {
    for (int j = 0; j < len; j++)
      g[i].push_back(octopus[i][j] - '0');
  }

  for (int i = 0; i < sz; i++)
  {
    for (int j = 0; j < len; j++)
      cout <<  g[i][j] << " ";

    cout << "\n";
  }

  cout << "\n";

  for (int i = 0; i < 2; i++)
    ans += catch_flashes();

  cout << ans;

  return 0;
}