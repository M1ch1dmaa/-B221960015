import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class ThreeSum {
    public static List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> result = new HashSet<>();
        
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                for (int k = j + 1; k < nums.length; k++) {
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        List<Integer> triplet = Arrays.asList(nums[i], nums[j], nums[k]);
                        triplet.sort(Integer::compareTo); // Sort to handle duplicates
                        result.add(triplet);
                    }
                }
            }
        }
        
        return new ArrayList<>(result);
    }

    public static void main(String[] args) {
        int[] nums1 = {-1, 0, 1, 2, -1, -4};
        System.out.println(threeSum(nums1));

        int[] nums2 = {0, 1, 1};
        System.out.println(threeSum(nums2));

        int[] nums3 = {0, 0, 0};
        System.out.println(threeSum(nums3));
    }
}
