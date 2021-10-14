import Utils
import os.path


def add_score(difficulty):
    try:
        score = 0
        if os.path.exists(Utils.SCORES_FILE_NAME):
            score_file = open(Utils.SCORES_FILE_NAME, mode="r+")
            line = score_file.read()
            score = int(line)
            score_file.close()

        score_file = open(Utils.SCORES_FILE_NAME, mode="w+")
        print('Your previous score is %s points' % score)
        score += int(difficulty)
        print('Your new score is %s points' % score)
        score_file.write(str(score))
        score_file.close()
    except IOError:
        print(Utils.BAD_RETURN_CODE)
