#include <bits/stdc++.h>

using namespace std;

string s;
long long int lantern_fish_cnt[15], ans = 0;

int main(void)
{
  cin.tie(NULL);
  ios::sync_with_stdio(false);

  cin >> s;

  int len = s.length();

  for (int i = 0; i < len; i++)
  {
    if (s[i] >= '0' && s[i] <= '9')
      lantern_fish_cnt[s[i] - '0'] ++;
  }

  for (int i = 0; i < 256; i++)
  {
    long long int zc = lantern_fish_cnt[0];

    for (int j = 0; j < 8; j++)
      lantern_fish_cnt[j] = lantern_fish_cnt[j + 1];

    lantern_fish_cnt[6] += zc;
    lantern_fish_cnt[8] = zc;
  }

  for (int i = 0; i <= 8; i++)
    ans += lantern_fish_cnt[i];

  cout << ans;

  return 0;
}