import java.util.*;

public class Solution {
    public List<String> letterCombinations(String digits) {
      List<String> res = new ArrayList<>();
      if (digits.equals(""))
        return res;

      Map<Integer, String> dict1 = new HashMap<>();
      dict1.put(2, "abc");
      dict1.put(3, "def");
      dict1.put(4, "ghi");
      dict1.put(5, "jkl");
      dict1.put(6, "mno");
      dict1.put(7, "pqrs");
      dict1.put(8, "tuv");
      dict1.put(9, "wxyz");

      String letter_string = dict1.get(Integer.parseInt(digits.substring(0, 1)));

      if (digits.length() > 1) {
        List<String> sub_output = letterCombinations(digits.substring(1));
        for (char c : letter_string.toCharArray()) {
          for (String output : sub_output) {
            res.add(c + output);
          }
        }
        return res;
      }
      else {
        for (char c : letter_string.toCharArray()) {
          res.add(String.valueOf(c));
        }
        return res;
      }
    }
}