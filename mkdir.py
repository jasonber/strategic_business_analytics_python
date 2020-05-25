import os
import re
import sys

def replace_line(x):
    return re.sub(r"[ :-]", "_", str(x))

def syst():
    x = input("选择你的操作系统:\n 1.win\n 2.linux\n 3.mac\n ")
    if x == "1":
        return "win"
    else: 
        return "other"


def coures1_dir(course1, sys):
    for course in course1.keys():
        c_name = replace_line(course)
        for week in course1[course].keys():
            w_name = replace_line(week)
            cls = course1[course][week]
            if type(cls) is dict:
                cls_name = replace_line(cls.keys().__iter__().__next__())
                for c in cls.values():
                    if type(c) is list:
                        for x in c:
                            cl_name = replace_line(x)
                            if sys == "win":
                                path = ".\\{}\\{}\\{}\\{}".format(c_name, w_name, str(cls_name), cl_name)
                            else:
                                path = "./{}/{}/{}/{}".format(c_name, w_name, str(cls_name), cl_name)
                            # print("list: {} \n {} ".format(c, path))
                            os.makedirs(path)
                    else:
                        cl_name = replace_line(c)
                        if sys == "win":
                            path = ".\\{}\\{}\\{}\\{}".format(c_name, w_name, str(cls_name), cl_name)
                        else:
                            path = "./{}/{}/{}/{}".format(c_name, w_name, str(cls_name), cl_name)
                        # print("no list: {} \n {} ".format(c, path))
                        os.makedirs(path)
            else:
                cls_name = replace_line(cls)
                if sys == "win":
                    path = ".\\{}\\{}\\{}".format(c_name, w_name, cls_name)
                else:
                    path = "./{}/{}/{}".format(c_name, w_name, cls_name)
                # print("no dict:  ", path)
                os.makedirs(path)



def course2_dir(course1, sys):
    for course in course1.keys():
        c_name = replace_line(course)
        for week in course1[course].keys():
            w_name = replace_line(week)
            val = course1[course][week]
            if type(val) is list:
                for cls in val:
                    if type(cls) is dict:
                        cls_name = replace_line(
                            cls.keys().__iter__().__next__())
                        for cl in cls.values():
                            if type(cl) is list:
                                for x in cl:
                                    cl_name = replace_line(x)
                                    if sys == "win":
                                        path = ".\\{}\\{}\\{}\\{}".format(c_name, w_name, str(cls_name), cl_name)
                                    else:
                                        path = "./{}/{}/{}/{}".format(c_name, w_name, str(cls_name), cl_name) 
                                    # print("list: {} \n {} ".format(c, path))
                                    os.makedirs(path)
                            else:
                                cl_name = replace_line(x)
                                if sys == "win":
                                    path = ".\\{}\\{}\\{}\\{}".format(c_name, w_name, str(cls_name), cl_name)
                                else:
                                    path = "./{}/{}/{}/{}".format(c_name, w_name, str(cls_name), cl_name)
                                # print("no list: {} \n {} ".format(c, path))
                                os.makedirs(path)


def course3_dir(course3, sys):
    for course in course3.keys():
        c_name = replace_line(course)
        vls = course3[course]
        for i in vls:
            if type(i) is dict:
                w_name = replace_line(i.keys().__iter__().__next__())
                cls_name = replace_line(i.values())
                if sys == "win":
                    path = ".\\{}\\{}\\{}".format(c_name, w_name, cls_name)
                else:
                    path = "./{}/{}/{}".format(c_name, w_name, cls_name)
                os.makedirs(path)
            else:
                w_name = replace_line(i)
                if sys == 'win':
                    path = ".\\{}\\{}".format(c_name, w_name)
                else:
                    path = "./{}/{}".format(c_name, w_name)
                os.makedirs(path)


def run():
    sys = syst()
    coursera = {
        "Foundations of strategic business analytics":
        {
            "Week 1": "Practice Quiz",
            "Week 2":
            {
                "Factors leading to events: recitals":
                ["Recital M3 Credit score example",
                 "Recital M3 HR example"]
            },
            "Week 3":
            {
                "Predictions and Forecasting: recitals":
                ["Recital M4 - Credit Score", "Recital M4 - HR example",
                 "Recital M4 - Predictive maintenance example",
                 "Recital M4 - Chocolate Sales example"]
            },
            "Week 4":
            {
                "Recommendation production and prioritization: recital":
                "Recital M5 - How to present your findings"
            }
        },
        "Foundations of Marketing Analytics":
        {
            "Week 1": "Welcome to the course",
            "Week 2":
            [
                {
                    "Statistical segmentation: lectures and recitals":
                    ["Computing recency, frequency and monetary value with R (Recital 1)",
                     "Preparing and transforming your data in R (Recital 2)",
                     "Running a hierarchical segmentation in R (Recital 3)"]
                },
                "Statistical segmentation: Graded Assessment 1"
            ],
            "Week 3":
            [
                {
                    "Managerial segmentation: lectures and recitals":
                    ["LectureCoding a managerial segmentation in R (Recital 1)",
                     "Segmenting a database retrospectively in R (Recital 2)",
                     "LectureR tutorial (Recital 3)"]
                },
                "Managerial segmentation: Graded Assessment 2"
            ],
            "Week 4":
            [
                {
                    "Targeting and scoring models: lectures and recitals":
                    "Building a predictive model in R (Recital)"
                },
                "Targeting and scoring models: Graded Assessment 3"
            ],
            "Week 5":
            [
                {
                    "Customer lifetime value: lectures and recitals":
                    ["How to compute a transition matrix in R (Recital 1)",
                     "Using the transition matrix to make predictions in R (Recital 2)",
                     "LectureComputing customer lifetime value in R (Recital 3)"]
                },
                "Customer lifetime value: Graded Assessment 4"
            ]
        },
        "Case studies in business analytics with ACCENTURE":
        [
            {
                "Week 1": "Graded assignment 1",
            },
            "Week 2",
            {
                "Week 3": "Graded Assignment 2"
            }
        ]
    }

    key_lst = list(coursera.keys())
    
    course1 = {key_lst[0]:coursera[key_lst[0]]}
    coures1_dir(course1, sys)

    course2 = {key_lst[1]:coursera[key_lst[1]]}
    course2_dir(course2, sys)

    course3 = {key_lst[2]:coursera[key_lst[2]]}
    course3_dir(course3, sys)

    print("create dirtory successfully")

if __name__ == "__main__":
    run()
    
