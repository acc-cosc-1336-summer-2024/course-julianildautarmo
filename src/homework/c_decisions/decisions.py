def get_options_ratio(option,total):
    
    ratio = float(option)/float(total)
    
    return ratio



def get_faculty_rating(ratio):

    if(ratio < 1.0 and ratio >= 0.9):
        rating="Excellent"

    elif(ratio < 0.9 and ratio >= 0.8):
        rating="Very Good"

    elif(ratio < 0.8 and ratio >= 0.7):
        rating="Good"
       
    elif(ratio < 0.7 and ratio >= 0.6):
        rating="Needs Improvement"

    else:
        rating="Unacceptable"

    return rating