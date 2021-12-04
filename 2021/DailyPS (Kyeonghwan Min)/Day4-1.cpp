#include <bits/stdc++.h>

using namespace std;

string s;
vector<int> ball;
int bingo[7][7];

int main(void)
{
  cin.tie(NULL);
  ios::sync_with_stdio(false);

  cin >> s;

  int len = s.length();
  int tmp = 0;

  for (int i = 0; i < len; i++)
  {
    if (s[i] >= '0' && s[i] <= '9')
      tmp = tmp * 10 + (s[i] - '0');

    else
    {
      ball.push_back(tmp);
      tmp = 0;
    }
  }

  ball.push_back(tmp);

  int sz = ball.size();
  int min_ball_cnt = INT_MIN;
  int ans = 0;

  while(!cin.eof() && cin.good())
  {
    for (int i = 0; i < 5; i++)
    {
      for (int j = 0; j < 5; j++)
        cin >> bingo[i][j];
    }

    int ball_cnt = 0;
    int row_correct[7] = { 0 };
    int col_correct[7] = { 0 };
    bool made_bingo = false, ball_correct[7][7] = { 0 };

    for (ball_cnt = 0; ball_cnt < sz; ball_cnt++)
    {
      for (int j = 0; j < 5; j++)
      {
        for (int k = 0; k < 5; k++)
        {
          if (bingo[j][k] == ball[ball_cnt])
          {
            row_correct[j]++;
            col_correct[k]++;
            ball_correct[j][k] = true;
          }
        }
      }

      for (int j = 0; j < 5; j++)
      {
        if (row_correct[j] == 5 || col_correct[j] == 5)
        {
          made_bingo = true;
          break;
        }
      }

      if (made_bingo)
        break;
    }

    if (min_ball_cnt > ball_cnt)
      min_ball_cnt = ball_cnt;

    else
      continue;

    int sum = 0;

    for (int i = 0; i < 5; i++)
    {
      for (int j = 0; j < 5; j++)
      {
        if (!ball_correct[i][j])
          sum += bingo[i][j];
      }
    }

    ans = sum * ball[ball_cnt];
  }

  cout << ans;

  return 0;
}