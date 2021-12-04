#include <bits/stdc++.h>

using namespace std;

long long int width = 0, depth = 0;

int main(void)
{
  cin.tie(NULL);
  ios::sync_with_stdio(false);

  while(!cin.eof() && cin.good())
  {
    string command;
    long long int num;

    cin >> command >> num;

    if (!command.compare("forward"))
      width += num;

    else if (!command.compare("down"))
      depth += num;

    else if (!command.compare("up"))
      depth -= num;
  }

  cout << width * depth;

  return 0;
}