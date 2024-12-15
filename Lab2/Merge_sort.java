import org.junit.jupiter.api.Test;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class MergeSortTest {

    public static int[] mergeSort(int[] arr) {
        if (arr.length > 1) {
            int mid = arr.length / 2;

            int[] left = Arrays.copyOfRange(arr, 0, mid);
            int[] right = Arrays.copyOfRange(arr, mid, arr.length);

            mergeSort(left);
            mergeSort(right);

            int i = 0, j = 0, k = 0;

            while (i < left.length && j < right.length) {
                if (left[i] < right[j]) {
                    arr[k++] = left[i++];
                } else {
                    arr[k++] = right[j++];
                }
            }

            while (i < left.length) {
                arr[k++] = left[i++];
            }

            while (j < right.length) {
                arr[k++] = right[j++];
            }
        }
        return arr;
    }

    @Test
    public void testMergeSort() throws IOException {
        // Define the file path
        File file = new File("test.txt");

        // Read the file
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line = br.readLine();

            // Parse the input from the file
            String[] parts = line.split("\\s{4}"); // Splits on 4 spaces
            int[] unsortedArray = Arrays.stream(parts[0].replace("[", "").replace("]", "").split(","))
                                         .map(String::trim)
                                         .mapToInt(Integer::parseInt)
                                         .toArray();
            int[] sortedArray = Arrays.stream(parts[1].replace("[", "").replace("]", "").split(","))
                                       .map(String::trim)
                                       .mapToInt(Integer::parseInt)
                                       .toArray();

            // Assert the result
            assertArrayEquals(sortedArray, mergeSort(unsortedArray));
        }
    }
}
