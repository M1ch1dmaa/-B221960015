import org.junit.jupiter.api.Test;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class InsertionSortTest {

    public static int[] insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && key < arr[j]) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
        return arr;
    }

    @Test
    public void testInsertionSort() throws IOException {
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
            assertArrayEquals(sortedArray, insertionSort(unsortedArray));
        }
    }
}
