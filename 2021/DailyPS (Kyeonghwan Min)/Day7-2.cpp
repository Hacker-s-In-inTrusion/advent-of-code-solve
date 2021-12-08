#include <bits/stdc++.h>
#include <limits.h>

using namespace std;

vector<long long int> v;

long long int ans = LLONG_MAX;

int main(void)
{
  cin.tie(NULL);
  ios::sync_with_stdio(false);

  string s;
  cin >> s;

  int len = s.length();
  int tmp = 0;

  for (int i = 0; i < len; i++)
  {
    if (s[i] >= '0' && s[i] <= '9')
      tmp = tmp * 10 + (s[i] - '0');

    else
    {
      v.push_back(tmp);
      tmp = 0;
    }
  }

  v.push_back(tmp);

  sort(v.begin(), v.end());

  int sz = v.size();

  int hmin = 0;
  int hmax = v[sz - 1];

  for (int i = hmin; i < hmax; i++)
  {
    long long int tmp = 0;

    for (int j = 0; j < sz; j++)
    {
      long long int diff = abs(i - v[j]);
      tmp += diff * (diff + 1) / 2;
    }

    ans = min(ans, tmp);
  }

  cout << ans;

  return 0;
}