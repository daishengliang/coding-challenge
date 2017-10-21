"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

"""
class Solution(object):
    def readBinaryWatch(self, num):
        """
        10盏灯泡的燃亮情况可以通过0-1024进行表示，然后计数二进制1的个数即可。
        http://bookshadow.com/weblog/2016/09/18/leetcode-binary-watch/
        :type num: int
        :rtype: List[str]
        """
        
        res = []
        for i in range(1024):
            # bin(i).count('1')
            binary = bin(i)
            cnt = 0
            for s in binary:
                if s == '1':
                    cnt += 1
            if cnt == num:
                res += self.parseTime(i)
        return res
        
    def parseTime(self, num):
        hour, minute = num >> 6, num & 0x3F
        if hour > 11 or minute > 59:
            return []
        return [str(hour) + ':' + str(minute).zfill(2)]

class Solution2 {
public:
    vector<string> readBinaryWatch(int num) {
        vector<string> res;
        vector<int> hour{8, 4, 2, 1}, minute{32, 16, 8, 4, 2, 1};
        for (int i = 0; i <= num; ++i) {
            vector<int> hours = generate(hour, i);
            vector<int> minutes = generate(minute, num - i);
            for (int h : hours) {
                if (h > 11) continue;
                for (int m : minutes) {
                    if (m > 59) continue;
                    res.push_back(to_string(h) + (m < 10 ? ":0" : ":") + to_string(m));
                }
            }
        }
        return res;
    }
    vector<int> generate(vector<int>& nums, int cnt) {
        vector<int> res;
        helper(nums, cnt, 0, 0, res);
        return res;
    }
    void helper(vector<int>& nums, int cnt, int pos, int out, vector<int>& res) {
        if (cnt == 0) {
            res.push_back(out);
            return;
        }
        for (int i = pos; i < nums.size(); ++i) {
            helper(nums, cnt - 1, i + 1, out + nums[i], res);
        }
    }
};