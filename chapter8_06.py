def solution(genres, plays):
    answer = []
    genre_dict = {}
    play_dict = {}

    # 장르별 총 재생 횟수와 각 곡의 재생 횟수 저장
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in genre_dict:
            genre_dict[genre] = []
            play_dict[genre] = 0
        genre_dict[genre].append((i, play))
        play_dict[genre] += play

    # 총 재생 회수가 많은 장르순으로 정렬하는 함수
    def get_play_count(item):
        return item[1]

    sorted_genres = sorted(play_dict.items(), key=get_play_count, reverse=True)

    # 각 장르 내에서 노래를 재생 횟수 순으로 정렬하는 함수
    def sort_songs(song):
        return (-song[1], song[0])

    # 각 장르별로 최대 2곡씩 선택
    for genre, _ in sorted_genres:
        sorted_songs = sorted(genre_dict[genre], key=sort_songs)
        answer.extend([idx for idx, _ in sorted_songs[:2]])

    print(answer)
    return answer


# case 1

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

solution(genres, plays)
