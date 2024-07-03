#include <stdio.h>
#include <fpdfview.h>


#include "wrapper.h"


#define RESOLUTION_MULTIPLIER  4.1;

pdf_size get_pdf_page_size(int pageno, char* filename) {
     FPDF_InitLibrary(NULL);
    FPDF_DOCUMENT doc = FPDF_LoadDocument(filename, NULL);
    FPDF_PAGE page = FPDF_LoadPage(doc, pageno);
    int width = FPDF_GetPageWidth(page) * RESOLUTION_MULTIPLIER;
    int height = FPDF_GetPageHeight(page) * RESOLUTION_MULTIPLIER;
    pdf_size size;
    size.height = height;
    size.width = width;
    FPDF_DestroyLibrary();
    return size;
}


char* get_pdf_page(int pageno, char* filename) {
     FPDF_InitLibrary(NULL);
    FPDF_DOCUMENT doc = FPDF_LoadDocument(filename, NULL);
    FPDF_PAGE page = FPDF_LoadPage(doc, pageno);
    int width = FPDF_GetPageWidth(page) * RESOLUTION_MULTIPLIER;
    int height = FPDF_GetPageHeight(page) * RESOLUTION_MULTIPLIER;
    FPDF_BITMAP bitmap = FPDFBitmap_Create(width, height, 0);
    FPDFBitmap_FillRect(bitmap, 0, 0, width, height, 0xFFFFFFFF);
    FPDF_RenderPageBitmap(bitmap, page, 0, 0, width, height, 0, FPDF_GRAYSCALE);
    char *pixels = (char*)FPDFBitmap_GetBuffer(bitmap);
    FPDF_DestroyLibrary();
    return pixels;
}


