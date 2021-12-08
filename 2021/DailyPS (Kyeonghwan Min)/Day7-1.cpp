#include <bits/stdc++.h>

using namespace std;

vector<long long int> v;

long long int ans = 0;

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
  int mid = sz / 2;

  for (int i = 0; i < sz; i++)
    ans += abs(v[mid] - v[i]);

  cout << ans;

  return 0;
}