def solution(id_list, report, k):
    len_id = len(id_list)
    report_user = [set() for _ in range(len_id)]
    mail = [0] * len_id
    for report_one in report:
        repo, stop = report_one.split()
        report_user[id_list.index(stop)].add(repo)
    for users in report_user:
        if len(users) >= k:
            for user in users:
                mail[id_list.index(user)] += 1

    answer = mail
    return answer