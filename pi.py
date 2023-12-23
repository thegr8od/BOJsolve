import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import RANSACRegressor
from scipy.optimize import minimize

# 데이터 파일 경로 설정
plane_file_path = 'C:\\Users\\김승준\\Desktop\\code\\data_file\\plane_fit_sample_data_with_delimiter_comma.txt'

# 데이터 로딩
plane_data = np.loadtxt(plane_file_path, delimiter=',')

# X, Y, Z 좌표 분리
X_plane = plane_data[:, 0].reshape(-1, 1)
Y_plane = plane_data[:, 1].reshape(-1, 1)
Z_plane = plane_data[:, 2]

# RANSAC 회귀
ransac_plane = RANSACRegressor()
XY_plane = np.hstack((X_plane, Y_plane))
ransac_plane.fit(XY_plane, Z_plane)
inlier_mask_plane = ransac_plane.inlier_mask_
outlier_mask_plane = np.logical_not(inlier_mask_plane)

# 평면 시각화를 위한 그리드 생성
xx, yy = np.meshgrid(np.linspace(X_plane.min(), X_plane.max(), 10),
                     np.linspace(Y_plane.min(), Y_plane.max(), 10))

# RANSAC 평면 추정
zz_ransac = ransac_plane.predict(np.hstack((xx.ravel().reshape(-1, 1), yy.ravel().reshape(-1, 1))))
zz_ransac = zz_ransac.reshape(xx.shape)

# TLS 방법을 위한 함수 정의 및 최적화
def distance_point_to_plane(plane_coeff, point):
    a, b, c, d = plane_coeff
    x, y, z = point
    return abs(a*x + b*y + c*z + d) / np.sqrt(a**2 + b**2 + c**2)

def total_squared_distance(plane_coeff, points):
    return sum(distance_point_to_plane(plane_coeff, point)**2 for point in points)

initial_guess = [1, 1, 1, 1]
result = minimize(total_squared_distance, initial_guess, args=(plane_data,))

# TLS 평면 계수
a, b, c, d = result.x
zz_tls = (-a*xx - b*yy - d) / c

# 3D 플로팅: RANSAC과 TLS 비교
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# RANSAC 평면
ransac_surface = ax.plot_surface(xx, yy, zz_ransac, color='cornflowerblue', alpha=0.5)

# TLS 평면
tls_surface = ax.plot_surface(xx, yy, zz_tls, color='red', alpha=0.5)

# 포인트 플로팅
ax.scatter(X_plane[inlier_mask_plane], Y_plane[inlier_mask_plane], Z_plane[inlier_mask_plane], color='yellowgreen', marker='.', label='Inliers')
ax.scatter(X_plane[outlier_mask_plane], Y_plane[outlier_mask_plane], Z_plane[outlier_mask_plane], color='gold', marker='.', label='Outliers')

# 레이블 추가
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("RANSAC vs TLS ")

# 범례 추가
ax.legend([ransac_surface, tls_surface], ['RANSAC Plane', 'TLS Plane'])

plt.show()
