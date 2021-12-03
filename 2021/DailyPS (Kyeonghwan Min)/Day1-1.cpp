#include <bits/stdc++.h>

using namespace std;

int prev_depth = 0;
int ans = 0;

int main(void)
{
  cin.tie(NULL);
  ios::sync_with_stdio(false);

  while (!cin.eof() && cin.good())
  {
    int depth;
    cin >> depth;

    if (prev_depth == 0)
    {
      prev_depth = depth;
      continue;
    }

    if (depth > prev_depth)
    {
      ans++;
      prev_depth = depth;
    }

    else
      prev_depth = depth;
  }

  cout << ans;

  return 0;
}