import prisma from "../../config/prisma";

const generateCompanyCode = () => {
    return "INFV-" + Math.random().toString(36).substring(2, 8).toUpperCase();
}
export const reGenerateCompanyCode = async (companyId: string) => {
    const newCode = generateCompanyCode();

    return prisma.company.update({
        where: { id: companyId },
        data: { code: newCode },
        select: {
            name: true,
            code: true,
        }
    })
}