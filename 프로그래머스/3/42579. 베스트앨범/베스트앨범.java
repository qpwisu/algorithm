import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        
        class GenreInfo {
            int totalPlays = 0;
            List<int[]> songs = new ArrayList<>();  // [index, play]

            public void addSong(int index, int playCount) {
                totalPlays += playCount;
                songs.add(new int[]{index, playCount});
            }
        }

        Map<String, GenreInfo> genreMap = new HashMap<>();

        // 1. Map에 장르별 정보 저장
        for (int i = 0; i < genres.length; i++) {
            genreMap.putIfAbsent(genres[i], new GenreInfo());
            genreMap.get(genres[i]).addSong(i, plays[i]);
        }

        // 2. 장르를 총 재생 수 기준으로 정렬
        List<String> genreOrder = new ArrayList<>(genreMap.keySet());
        genreOrder.sort((g1, g2) -> genreMap.get(g2).totalPlays - genreMap.get(g1).totalPlays);

        // 3. 각 장르마다 재생 수 많은 노래 2개 뽑기
        List<Integer> result = new ArrayList<>();
        for (String genre : genreOrder) {
            List<int[]> songs = genreMap.get(genre).songs;
            songs.sort((a, b) -> {
                if (b[1] == a[1]) return a[0] - b[0]; // 재생수 같으면 인덱스 오름차순
                return b[1] - a[1]; // 재생수 내림차순
            });

            for (int i = 0; i < Math.min(2, songs.size()); i++) {
                result.add(songs.get(i)[0]);
            }
        }

        // 4. 리스트를 배열로 변환
        return result.stream().mapToInt(i -> i).toArray();
    }
}