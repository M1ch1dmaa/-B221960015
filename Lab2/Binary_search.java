import org.junit.jupiter.api.Test;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class BinarySearchTest {

    public static int binarySearch(int[] arr, int low, int high, int x) {
        if (high >= low) {
            int mid = low + (high - low) / 2;

            if (arr[mid] == x) {
                return mid;
            } else if (arr[mid] > x) {
                return binarySearch(arr, low, mid - 1, x);
            } else {
                return binarySearch(arr, mid + 1, high, x);
            }
        } else {
            return -1;
        }
    }

    @Test
    public void testBinarySearch() throws IOException {
        // Define the file path
        File file = new File("testbinary.txt");

        // Read the file
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line = br.readLine();

            // Parse the input from the file
            String[] parts = line.split("\\s{4}"); // Splits on 4 spaces
            int[] array = Arrays.stream(parts[0].replace("[", "").replace("]", "").split(","))
                                 .map(String::trim)
                                 .mapToInt(Integer::parseInt)
                                 .toArray();
            int expected = Integer.parseInt(parts[1].trim());

            // Assert the result
            assertEquals(expected, binarySearch(array, 0, array.length - 1, 7));
        }
    }
}
