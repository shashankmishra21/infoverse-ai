import { Request, Response, NextFunction } from "express";
import jwt from "jsonwebtoken";

const JWT_SECRET = process.env.JWT_SECRET as string;

export interface AuthRequest extends Request {
  user?: {
    userId: string;
    companyId: string;
    role: "ADMIN" | "USER";
  };
}

export const authenticate = (req: AuthRequest, res: Response, next: NextFunction) => {
  const JWT_SECRET = process.env.JWT_SECRET;

  console.log("AUTH HEADER:", req.headers.authorization);

  if (!JWT_SECRET) { return res.status(500).json({ error: "JWT_SECRET not configured" });}

  const header = req.headers.authorization;

  if (!header || !header.startsWith("Bearer ")) {
    console.log("NO TOKEN");
    return res.status(401).json({ error: "No token provided" });
  }

  const token = header.split(" ")[1];
  try {
    const decoded = jwt.verify(token, JWT_SECRET) as any;
    console.log("DECODED:", decoded);
    req.user = decoded;
    next();
  } catch (err) {
    console.log("JWT ERROR:", err);
    return res.status(401).json({ error: "Invalid or expired token" });
  }
};