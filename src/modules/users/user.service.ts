import prisma from '../../config/prisma'

export const getCompanyUsers = async (companyId: string) => {
    return prisma.user.findMany({
        where: { companyId },
        select: {
            id: true,
            name: true,
            email: true,
            role: true,
            createdAt: true,
        }
    })
}