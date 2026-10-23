"use client";
import * as Dialog from "@radix-ui/react-dialog";
import Image from "next/image";
import type { Product } from "@/lib/products";
import { Arrow } from "./Arrow";

export function ProductDetails({
  product,
  light = false,
}: {
  product: Product;
  light?: boolean;
}) {
  return (
    <Dialog.Root>
      <Dialog.Trigger
        className={`detail-trigger ${light ? "light" : ""}`}
        aria-label={`Подробнее о ${product.name}`}
      >
        <span>Исследовать модель</span>
        <span className="circle-arrow">
          <Arrow diagonal />
        </span>
      </Dialog.Trigger>
      <Dialog.Portal>
        <Dialog.Overlay className="dialog-overlay" />
        <Dialog.Content
          className="product-dialog"
          aria-describedby={`description-${product.id}`}
        >
          <Dialog.Close
            className="dialog-close"
            aria-label="Закрыть подробности"
          >
            <svg width="24" height="24" viewBox="0 0 24 24" aria-hidden="true">
              <path
                d="m6 6 12 12M6 18 18 6"
                stroke="currentColor"
                strokeWidth="1.5"
              />
            </svg>
          </Dialog.Close>
          <div className="dialog-image">
            <Image
              src={product.image}
              alt={product.imageAlt}
              width={500}
              height={500}
              sizes="(max-width: 700px) 70vw, 400px"
            />
          </div>
          <div className="dialog-copy">
            <p className="micro">{product.category}</p>
            <Dialog.Title>{product.name}</Dialog.Title>
            <Dialog.Description id={`description-${product.id}`}>
              {product.description}
            </Dialog.Description>
            <dl className="spec-list">
              {product.specs.map(([label, value]) => (
                <div key={label}>
                  <dt>{label}</dt>
                  <dd>{value}</dd>
                </div>
              ))}
            </dl>
            <p className="spec-note">{product.note}</p>
            <a
              className="button button-dark"
              href={product.url}
              target="_blank"
              rel="noopener noreferrer"
            >
              На официальный сайт <Arrow diagonal />
            </a>
          </div>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
