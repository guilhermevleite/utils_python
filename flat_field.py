import cv2 as cv
import numpy as np

# img = cv.imread('/home/leite/Downloads/placa62705/F1.tif')
# img = cv.resize(img, (256, 256))

# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
#
# clahe = cv.createCLAHE(clipLimit=5)
# final = clahe.apply(lab[:, :, 0])
#
# # CLAHE
# cla = np.copy(lab)
# cla[:, :, 0] = final
#
# cla = cv.cvtColor(cla, cv.COLOR_LAB2BGR)
#
# equa = cv.equalizeHist(lab[:, :, 0])
# aux = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
# equa = cv.equalizeHist(cv.cvtColor(aux, cv.COLOR_BGR2GRAY))
# # equa = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
# equa = cv.cvtColor(equa, cv.COLOR_GRAY2BGR)
#
# conc = cv.hconcat([img, cla])
# dummy = cv.hconcat([equa, equa])
# conc = cv.vconcat([conc, dummy])
# cv.imshow("window", conc)
# cv.waitKey(0)

#include <opencv2/core.hpp>
# #include <vector>       // std::vector
# int main(int argc, char** argv)
# {
#     // READ RGB color image and convert it to Lab
#     cv::Mat bgr_image = cv::imread("image.png");
#     cv::Mat lab_image;
#     cv::cvtColor(bgr_image, lab_image, CV_BGR2Lab);
#
#     // Extract the L channel
#     std::vector<cv::Mat> lab_planes(3);
#     cv::split(lab_image, lab_planes);  // now we have the L image in lab_planes[0]
#
#     // apply the CLAHE algorithm to the L channel
#     cv::Ptr<cv::CLAHE> clahe = cv::createCLAHE();
#     clahe->setClipLimit(4);
#     cv::Mat dst;
#     clahe->apply(lab_planes[0], dst);
#
#     // Merge the the color planes back into an Lab image
#     dst.copyTo(lab_planes[0]);
#     cv::merge(lab_planes, lab_image);
#
#    // convert back to RGB
#    cv::Mat image_clahe;
#    cv::cvtColor(lab_image, image_clahe, CV_Lab2BGR);
#
#    // display the results  (you might also want to see lab_planes[0] before and after).
#    cv::imshow("image original", bgr_image);
#    cv::imshow("image CLAHE", image_clahe);
#    cv::waitKey();
# }


def imflatfield(I, sigma):
    """Python equivalent imflatfield implementation
       I format must be BGR and type of I must be uint8"""
    A = I.astype(np.float32) / 255  # A = im2single(I);
    Ihsv = cv.cvtColor(A, cv.COLOR_BGR2HSV)  # Ihsv = rgb2hsv(A);
    A = Ihsv[:, :, 2]  # A = Ihsv(:,:,3);

    filterSize = int(2*np.ceil(2*sigma) + 1)

    # shading = imgaussfilt(A, sigma, 'Padding', 'symmetric', 'FilterSize', filterSize); % Calculate shading
    shading = cv.GaussianBlur(A, (filterSize, filterSize), sigma, borderType=cv.BORDER_REFLECT)

    meanVal = np.mean(A)  # meanVal = mean(A(:),'omitnan')

    #% Limit minimum to 1e-6 instead of testing using isnan and isinf after division.
    shading = np.maximum(shading, 1e-6)  # shading = max(shading, 1e-6);

    B = A*meanVal / shading  # B = A*meanVal./shading;

    C = np.copy(B)
    #% Put processed V channel back into HSV image, convert to RGB
    Ihsv[:, :, 2] = B  # Ihsv(:,:,3) = B;

    B = cv.cvtColor(Ihsv, cv.COLOR_HSV2BGR)  # B = hsv2rgb(Ihsv);

    B = np.round(np.clip(B*255, 0, 255)).astype(np.uint8)  # B = im2uint8(B);

    return B, shading


img = cv.imread('/home/leite/Downloads/placa62705/H2.tif')
img = cv.resize(img, (256, 256))
# Read input imgae
sigma = 20

out2, flat = imflatfield(img, sigma)

# cv2.imwrite('imflatfield_py_destroyer.png', out2)

flat = cv.cvtColor(flat, cv.COLOR_GRAY2BGR)
print(img.shape, out2.shape, flat.shape)
conc = cv.hconcat([img, out2])
cv.imshow("window", conc)
cv.imshow("window2", flat)
cv.waitKey(0)
