student_name = "Đào Duy Anh"
math_score = 7.0
science_score = 6.5

# Solution 1:
print("Tên: " + student_name + ", Điểm Toán: " + str(math_score) + ", Điểm Khoa học: " + str(science_score))


# Solution 2:
print(f"Tên: {student_name}, Điểm Toán: {math_score}, Điểm Khoa học: {science_score}")

sum_score = math_score + science_score
sub_score = math_score - science_score
multiply_score = math_score * science_score
divide_score = math_score / science_score

print(f"Tổng điểm: {sum_score}")
print(f"Hiệu điểm: {sub_score}")
print(f"Tích điểm: {multiply_score}")
print(f"Thương điểm: {divide_score:.2f}")  # Format to 2 decimal places

math_score += 1.0  # Increase math score by 1
print(f"Điểm Toán sau khi cộng thêm 1: {math_score}")

average_score = (math_score + science_score) / 2

if average_score >= 8.0:
    print("Xuất sắc")
elif average_score >= 6.5:
    print("Khá")
elif average_score >= 5.0:
    print("Trung bình")
else:
    print("Cần cố gắng")
