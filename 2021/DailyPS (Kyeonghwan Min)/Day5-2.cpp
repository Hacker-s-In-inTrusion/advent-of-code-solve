#include <bits/stdc++.h>

using namespace std;

int board[1005][1005];
int ans = 0;

vector<int> coor[4];

int main(void)
{
  cin.tie(NULL);
  ios::sync_with_stdio(false);

  while(!cin.eof() && cin.good())
  {
    string s1, s2, arrow;
    cin >> s1 >> arrow >> s2;

    int len1 = s1.length();
    int len2 = s2.length();
    int tmp = 0;
    int idx = 0;

    if (len1 == 0 || len2 == 0)
      break;

    for (int i = 0; i < len1; i++)
    {
      if (s1[i] >= '0' && s1[i] <= '9')
        tmp = tmp * 10 + s1[i] - '0';

      else
      {
        coor[idx].push_back(tmp);
        tmp = 0;
        idx++;
      }
    }

    coor[idx].push_back(tmp);
    tmp = 0;
    idx++;

    for (int i = 0; i < len2; i++)
    {
      if (s2[i] >= '0' && s2[i] <= '9')
        tmp = tmp * 10 + s2[i] - '0';

      else
      {
        coor[idx].push_back(tmp);
        tmp = 0;
        idx++;
      }
    }

    coor[idx].push_back(tmp);
  }

  int sz = coor[0].size();

  for (int i = 0; i < sz; i++)
  {
    if (coor[0][i] == coor[2][i])
    {
      if (coor[1][i] >= coor[3][i])
      {
        for (int j = coor[3][i]; j <= coor[1][i]; j++)
          board[j][coor[0][i]]++;
      }

      else
      {
        for (int j = coor[1][i]; j <= coor[3][i]; j++)
          board[j][coor[0][i]]++;
      }
    }

    else if (coor[1][i] == coor[3][i])
    {
      if (coor[0][i] >= coor[2][i])
      {
        for (int j = coor[2][i]; j <= coor[0][i]; j++)
          board[coor[1][i]][j]++;
      }

      else
      {
        for (int j = coor[0][i]; j <= coor[2][i]; j++)
          board[coor[1][i]][j]++;
      }
    }

    if (abs(coor[0][i] - coor[2][i]) == abs(coor[1][i] - coor[3][i]))
    {
      int diff = abs(coor[0][i] - coor[2][i]);
      int x_change = (coor[2][i] - coor[0][i]) / diff;
      int y_change = (coor[3][i] - coor[1][i]) / diff;

      int nx = coor[0][i];
      int ny = coor[1][i];
      
      for (int j = 0; j <= diff; j++)
      {
        board[ny][nx]++;
        nx += x_change;
        ny += y_change;
      }
    }
  }

  for (int i = 0; i < 1005; i++)
  {
    for (int j = 0; j < 1005; j++)
    {
      if (board[i][j] >= 2)
        ans++;
    }
  }

  cout << ans;

  return 0;
}