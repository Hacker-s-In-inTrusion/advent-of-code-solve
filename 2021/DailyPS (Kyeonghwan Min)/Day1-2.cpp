#include <bits/stdc++.h>

using namespace std;

int prev_depth_sum = 0;
int depth_sum = 0;
int ans = 0;

queue<int> depth_list;

int main(void)
{
  cin.tie(NULL);
  ios::sync_with_stdio(false);

  for (int i = 0; i < 3; i++)
  {
    int depth;
    cin >> depth;

    prev_depth_sum += depth;
    depth_sum += depth;
    depth_list.push(depth);
  }

  while (!cin.eof() && cin.good())
  {
    int depth;
    cin >> depth;

    depth_sum -= depth_list.front();
    depth_sum += depth;
    depth_list.pop();
    depth_list.push(depth);

    if (depth_sum > prev_depth_sum)
    {
      ans++;
      prev_depth_sum = depth_sum;
    }

    else
      prev_depth_sum = depth_sum;
  }

  cout << ans;

  return 0;
}