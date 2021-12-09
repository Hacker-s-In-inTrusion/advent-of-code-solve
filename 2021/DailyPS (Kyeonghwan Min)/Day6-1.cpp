#include <bits/stdc++.h>

using namespace std;

string s;
vector<int> lanternfish;

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
      lanternfish.push_back(tmp);
      tmp = 0;
    }
  }
  
  lanternfish.push_back(tmp);

  for (int i = 0; i < 80; i++)
  {
    int sz = lanternfish.size();
    int zc = 0;

    for (int j = 0; j < sz; j++)
    {
      if (lanternfish[j] != 0)
        lanternfish[j]--;

      else
      {
        lanternfish[j] = 6;
        zc++;
      }
    }

    for (int j = 0; j < zc; j++)
      lanternfish.push_back(8);
  }

  cout << lanternfish.size();

  return 0;
}